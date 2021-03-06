from lingpy import *
from lingpy.compare.partial import Partial
from sys import argv

if 'all' in argv:
    fname='../output/A_Deepadung_'
else:
    fname='../output/D_Deepadung_'

try:
    part = Partial(fname+'partial.bin.tsv')
except:
    part = Partial(fname+'subset.tsv', segments='tokens')
    print('[i] loaded the file')
    part.get_partial_scorer(runs=10000)
    part.output('tsv', filename=fname+'partial.bin', ignore=[], prettify=False)
    print('[i] saved the scorer')
finally:
    part.partial_cluster(
            method='lexstat',
            threshold=0.55,
            ref='cogids',
            mode='global',
            gop=-2,
            cluster_method='infomap'
            )

part.output('tsv', filename=fname+'partial', prettify=False)
