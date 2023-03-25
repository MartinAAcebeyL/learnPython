#%%
"""filter mayor  to 5"""
from unicodedata import name


may_50 = lambda x:  x >= 5
list_may_50 = filter(may_50, [4,5,6,7,4,1,3])
for i in list_may_50:
    print(i)
# %%
"""filter womans"""
clients =[
    {
        'name':'susan',
        'sex':'F'
    },
    {
        'name':'martin',
        'sex':'M'
    },
    {
        'name':'susana',
        'sex':'F'
    }
]

filter_f = lambda x: x['sex'] == 'F'
filtrado = filter(filter_f, clients)

for i in filtrado:
    print(i)

