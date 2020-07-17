from lingpy import *
from sys import argv

if 'all' in argv:
    fname='../output/A_Deepadung_'
else:
    fname='../output/D_Deepadung_'

alms = Alignments(fname+'partial.tsv', ref='cogids')
alms.align()
alms.output('tsv', filename=fname+'aligned', prettify=False)
