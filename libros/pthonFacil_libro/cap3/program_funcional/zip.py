#%%
"""a function of duple and triple numbers of a lists"""
NUMBERS = [1,2,3,4,5]
duplos = lambda s: s*2
triples = lambda s: s*3

duplos_iterable = map(duplos, NUMBERS)
triples_iterable = map(triples, NUMBERS)

duplos_triples = zip(duplos_iterable, triples_iterable)
#print(duplos_triples)
for i in duplos_triples:
    print(i)
# %%
