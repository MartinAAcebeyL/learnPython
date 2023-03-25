#%%
"""suma de 2 numeros"""
f = lambda *args: sum(args)
f(45,5, 50)
# %%
"""area de un rectangulo"""
ares_rectangulo = lambda a,b: a*b
ares_rectangulo(4,5)
# %%
"""consulta a tabla"""
response = lambda campo, tabla, condicion: f"select {campo} from {tabla} where {condicion}"
response('nombres, tickes', 'persona', '> 18')
# %%
"""saca piojos de perros"""

f = lambda piojo, trabajo: f'al {piojo} le practicaremos {trabajo}'

f('pulga', 'matar')
# %%
