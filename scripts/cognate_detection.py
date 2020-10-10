from lexibank_deepadungpalaung import Dataset
from lingpy import *
from lingpy.compare.partial import Partial
from lingpy.evaluate.acd import bcubes

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

part.renumber('cog')


method = input('method: ')

# type 'cogid' or 'cog' for method to see a tree based on Deepadung et al.'s
# cognate judgements

if method == 'lexstatcogids':
    part.get_partial_scorer(runs=10000)
    part.partial_cluster(method='lexstat', ref="lexstatcogids", threshold=0.55)
elif method == 'lexstatcogid':
    part.get_scorer(runs=10000)
    part.cluster(method='lexstat', ref="lexstatcogid", threshold=0.55)
    bcubes(part, 'cogid', 'lexstatcogid')
elif method == 'scacogids':
    part.partial_cluster(method='sca', threshold=0.45, ref='scacogids')
elif method == 'scacogid':
    part.cluster(method='sca', ref="scacogid", threshold=0.45)
    bcubes(part, 'cogid', 'scacogid')

part.calculate('tree', ref= method)
print(method)
print(part.tree.asciiArt())

import csv

x = part.distances
taxa = part.taxa
filename = '../output/distmat_'+ method+'.csv'
with open(filename, 'w',encoding = 'utf-8') as f:
    writer = csv.writer(f)
    header_row = ['Language']
    header_row.extend(taxa)
    writer.writerow(header_row)
    for i in range(len(taxa)):
        li = [taxa[i]]
        li.extend(x[i])
        writer.writerow(li)
    
