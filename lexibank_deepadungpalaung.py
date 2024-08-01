import attr
from pathlib import Path

from pylexibank import Concept, Language, FormSpec, Lexeme
from pylexibank.dataset import Dataset as BaseDataset
from pylexibank.util import progressbar
from lingpy import Wordlist
from pyedictor import fetch

from clldutils.misc import slug
from unicodedata import normalize


@attr.s
class CustomConcept(Concept):
    Number = attr.ib(default=None)


@attr.s
class CustomLexeme(Lexeme):
    Partial_Cognacy = attr.ib(default=None)


@attr.s
class CustomLanguage(Language):
    Latitude = attr.ib(default=None)
    Longitude = attr.ib(default=None)
    SubGroup = attr.ib(default="Palaung")
    Family = attr.ib(default="Austro-Asiatic")
    Location = attr.ib(default=None)
    EthnicName = attr.ib(default=None)
    Abbreviation = attr.ib(default=None)


class Dataset(BaseDataset):
    dir = Path(__file__).parent
    id = "deepadungpalaung"
    concept_class = CustomConcept
    language_class = CustomLanguage
    lexeme_class = CustomLexeme
    form_spec = FormSpec(
            separators=',',
            )

    def cmd_download(self, args):
        print('updating ...')
        with open(self.raw_dir.joinpath("deepadungpalaung.tsv"), "w", encoding="utf-8") as f:
            f.write(fetch("deepadungpalaung"))

    def cmd_makecldf(self, args):
        args.writer.add_sources()

        concepts = {}
        for concept in self.conceptlists[0].concepts.values():
            idx = concept.id.split("-")[-1] + "_" + slug(concept.english)
            args.writer.add_concept(
                ID=idx,
                Name=concept.english,
                Number=concept.number,
                Concepticon_ID=concept.concepticon_id,
                Concepticon_Gloss=concept.concepticon_gloss,
            )
            concepts[concept.number] = idx
        languages = args.writer.add_languages(lookup_factory="Name")

        # we combine with the manually edited wordlist to retrieve the lexeme
        # values
        wl = Wordlist(self.raw_dir.joinpath('deepadungpalaung.tsv').as_posix())
        mapper = {(concept, language, normalize("NFD", form)): [segments, cogids] for (idx, concept,
                language, form, segments, cogids) in wl.iter_rows(
                    'concept', 'doculect', 'form', 'tokens', 'cogids')}
        data = self.raw_dir.read_csv('100item-phylo.Sheet1.csv', dicts=False)
        for i, row in progressbar(enumerate(data[4:])):
            number = row[0].strip().strip('.')
            concept = row[1].strip()
            for j in range(0, len(row)-2, 2):
                language = data[2][j+2]
                value = row[j+2]
                if value.strip() and value.strip() not in ['-----']:
                    if ',' in row[j+2]:
                        forms = [v.strip() for v in value.split(',')]
                        cogids = [str(int(float(x))) for x in row[j+3].split(' or ')]
                    else:
                        forms = [value.strip()]
                        cogids = [str(int(float(row[j+3].split(' or ')[0])))]

                    for form, cogid in zip(forms, cogids):
                        try:
                            segments, cogids = mapper[concept, languages[language], form]
                            lexeme = args.writer.add_form_with_segments(
                                    Parameter_ID=concepts[number],
                                    Language_ID=languages[language],
                                    Value=value.strip(),
                                    Form=form,
                                    Segments=segments,
                                    Source="Deepadung2015",
                                    Partial_Cognacy=" ".join([str(x) for x in cogids])
                                    )
                        except:
                            args.log.warn('lexeme missing {0} / {1} / {2}'.format(
                                        concept, language, form))
                            lexeme = args.writer.add_form(
                                    Parameter_ID=concepts[number],
                                    Language_ID=languages[language],
                                    Value=value.strip(),
                                    Form=form,
                                    Source="Deepadung2015",
                                    Partial_Cognacy=""
                                    )
                        args.writer.add_cognate(
                                lexeme=lexeme,
                                Cognateset_ID=cogid+'-'+number,
                                Source="Deepadung2015"
                                )
