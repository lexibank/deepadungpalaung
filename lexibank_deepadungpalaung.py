import attr
from pathlib import Path

from pylexibank import Concept, Language, FormSpec
from pylexibank.dataset import Dataset as BaseDataset
from pylexibank.util import progressbar

import lingpy
from clldutils.misc import slug


@attr.s
class CustomConcept(Concept):
    Number = attr.ib(default=None)


@attr.s
class CustomLanguage(Language):
    Latitude = attr.ib(default=None)
    Longitude = attr.ib(default=None)
    SubGroup = attr.ib(default="Palaung")
    Family = attr.ib(default="Austro-Asiatic")
    Location = attr.ib(default=None)
    EthnicName=attr.ib(default=None)
    Abbreviation=attr.ib(default=None)


class Dataset(BaseDataset):
    dir = Path(__file__).parent
    id = "deepadungpalaung"
    concept_class = CustomConcept
    language_class = CustomLanguage
    form_spec = FormSpec(
            separators=',',
            )

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

        # here we need to add the lexemes
        data = self.raw_dir.read_csv('100item-phylo.Sheet1.csv', dicts=False)
        for i, row in progressbar(enumerate(data[4:])):
            number = row[0].strip().strip('.')
            for j in range(0, len(row)-2, 2):
                language = data[2][j+2]
                value = row[j+2]
                if value.strip() and value.strip() not in ['-----']:
                    if not 'or' in row[3+j]:
                        cogid = str(int(float(row[j+3])))
                    else:
                        cogid = row[j+3].split()[0]
                    for lexeme in args.writer.add_forms_from_value(
                            Parameter_ID=concepts[number],
                            Language_ID=languages[language],
                            Value=value.strip(),
                            Source='Deepadung2015'):
                        args.writer.add_cognate(
                                lexeme=lexeme,
                                Cognateset_ID=cogid+'-'+number,
                                Source='Deepadung2015')

