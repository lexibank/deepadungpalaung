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
        columns=columns, namespace=namespace) #25

input('loaded data')

part.renumber('cog')  #26

from lingpy.evaluate.acd import bcubes #10

for i in range(20): #27
    t = 0.05 * i 
    ts = 't_'+str(i) 
    part.partial_cluster(method='sca', threshold=t, ref=ts) 
    part.add_cognate_ids(ts, ts+'id', idtype='strict') 
    p, r, f = bcubes(part, 'cogid', ts+'id', pprint=False) 
    print('{0:.2f}   {1:.4}   {2:.4f}   {3:.2f}'.format(t, p, r, f))

for i in range(20): #30
    t = 0.05 * i 
    ts = 't_'+str(i) 
    part.partial_cluster(method='sca', threshold=t, ref=ts) 
    part.add_cognate_ids(ts, ts+'id', idtype='loose') 
    p, r, f = bcubes(part, 'cogid', ts+'id', pprint=False) 
    print('{0:.2f}   {1:.4}   {2:.4f}   {3:.2f}'.format(t, p, r, f))     

alms = Alignments(part, ref='cogids')
alms.align()
alms.output('tsv', filename='../output/deepadung-wordlist-new2', ignore='all', prettify=False)
