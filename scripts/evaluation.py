from lingpy import *
from lexibank_deepadungpalaung import Dataset
from lingpy.evaluate.acd import bcubes

ds = Dataset()

wl = Wordlist.from_cldf(
        ds.dir.joinpath('cldf', 'cldf-metadata.json'),
        columns=[
            'language_id', 'concept_name', 'value', 'form', 'segments', 
            'cogid_cognateset_id'],
        namespace=dict([
            ['language_id', 'doculect'],
            ['concept_name', 'concept'],
            ['value', 'value'],
            ['form', 'form'],
            ['segments', 'tokens'],
            ['cogid_cognateset_id', 'cog']])
        )
wl.renumber('cog')

lex = LexStat(wl)
lex.get_scorer(runs=10000)
for i in range(1, 20):
    t = i * 0.05
    ts = '{0}'.format(int(t*100+0.5))
    lex.cluster(method='sca', threshold=t, ref='sca_'+ts, restricted_chars='')
    lex.cluster(method='lexstat', threshold=t, ref='ls_'+ts, restricted_chars='')
    p1, r1, f1 = bcubes(lex, 'cogid', 'sca_'+ts, pprint=False)
    p2, r2, f2 = bcubes(lex, 'cogid', 'ls_'+ts, pprint=False)
    print('\t'.join(['{0:.2f}'.format(x) for x in [t, p1, r1, f1, p2, r2, f2]]))
