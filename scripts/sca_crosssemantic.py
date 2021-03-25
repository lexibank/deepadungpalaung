from lingpy import *
from lingrex.colex import find_colexified_alignments, find_bad_internal_alignments
from lingrex.align import template_alignment
from sys import argv

if 'all' in argv:
    fname='../output/'
else:
    fname='../output/'


alms = Alignments(fname+'deepadung-wordlist-new.tsv', ref='cogids')
print('[i] search for bad internal alignments')
find_bad_internal_alignments(alms)

print('[i] search for colexified alignments')
find_colexified_alignments(
        alms,
        cognates='cogids',
        segments='tokens',
        ref='crossids'
        )

# re-align the data
print('[i] re-align the data')
alms = Alignments(alms, ref='crossids')
alms.align()

alms.output('tsv', filename=fname+'sca_crossids', prettify=False)
