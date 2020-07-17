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
part.get_partial_scorer(runs=100) # make tests with 100 and 1000, when debugging)
part.partial_cluster(method='lexstat', threshold=0.5, ref='cogids', cluster_method='infomap')
alms = Alignments(part, ref='cogids')
alms.align()
alms.output('tsv', filename='deepadung-wordlist', ignore='all', prettify=False)
