from lexibank_deepadungpalaung import Dataset
from lingpy import *
from lingpy.compare.partial import Partial

wl = Wordlist.from_cldf(Dataset().cldf_dir.joinpath('cldf-metadata.json'))
i = 0
for idx, tokens in wl.iter_rows('tokens'):
    #print(idx, tokens)
    for segment in tokens.n:
        if not segment:
            print(idx, tokens)

input('all fine')

columns=('concept_name', 'language_id',
                'value', 'form', 'segments', 'language_glottocode', 'cogid_cognateset_id'
                )
namespace=(('concept_name', 'concept'), ('language_id',
                'doculect'), ('segments', 'tokens'), ('language_glottocode',
                    'glottolog'), ('concept_concepticon_id', 'concepticon'),
                ('language_latitude', 'latitude'), ('language_longitude',
                    'longitude'), ('cognacy', 'cognacy'),
                ('cogid_cognateset_id', 'cog'))

part = Partial.from_cldf(Dataset().cldf_dir.joinpath('cldf-metadata.json'),
        columns=columns, namespace=namespace)

input('loaded data')

part.cluster(method='sca', ref="scacogid", threshold=0.45)
part.get_scorer(runs=100)
part.cluster(method='lexstat', ref="lexstatcogid", threshold=0.55)

from lingpy.evaluate.acd import bcubes

bcubes(part, "cogid", "scacogid")
bcubes(part, "cogid", "lexstatcogid")

alms = Alignments(part, ref='cogids')
alms.align()
alms.output('tsv', filename='deepadung-wordlist-sca', ignore='all', prettify=False)
