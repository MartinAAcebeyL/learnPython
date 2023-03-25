#%%
"""a function large of line"""
from functools import reduce


stadict_function = lambda *args: sum(args)/min(args)
print(reduce(stadict_function,[1,2,1]))

# %%
"""promedio section"""
prom = lambda *args: sum(args)
f = reduce(prom,[4,4,4,7])
print(f/4)
# %%
