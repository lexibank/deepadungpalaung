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

part.renumber('cog')  #8

from lingpy.evaluate.acd import bcubes #10

part.partial_cluster(method='sca', threshold=0.45, ref='scaids') #12

part.add_cognate_ids('scaids', 'scaid', idtype='strict') #13

bcubes(part, 'cogid', 'scaid') #15

part.add_cognate_ids('scaids', 'scalooseid', idtype='loose') #16

bcubes(part, 'cogid', 'scalooseid') #17

alms = Alignments(part, ref='cogid')
alms.align()
alms.output('tsv', filename='../output/deepadung-wordlist-new', ignore='all', prettify=False)
