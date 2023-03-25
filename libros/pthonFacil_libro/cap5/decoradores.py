#%%
"""
f(x) = x + 1
g(x) = 2*x
Calcular
f(g(x))

con x = [5,6,7]
"""

from re import A
from time import sleep


def f(g):
    def h(x):
        return g(x) + 1
    return h

@f
def g(x):
    return 2*x

print(g(5))
# %%

"""
a bank class with a active account
"""

cuentas = {
    '001': {'name': 'Juan', 'account': True},
    '002': {'name': 'Pedro', 'account': False},
    '003': {'name': 'Maria', 'account': False},
    '004': {'name': 'Ana', 'account': True}
    }

def search_account(func):
    """
    Decorador que busca una cuentas activas, inactivas y cuentas que no existen
    return status:
    -1 -> cuando la cuenta no existe
    0 -> cuando la cuenta ya estaba activa
    1 -> para activar la cuenta
    """
    def envolt(self, *args, **kwargs):
        if args[0] in self.get_account():
            if self.get_account()[args[0]]['account']:
                return func(self, id = args[0], status = 0)
            return func(self, id = args[0], status = 1)
        return func(self, id = args[0], status = -1)
    return envolt

class bank:
    __accounts = None

    def __init__(self) -> None:
        self.__accounts = cuentas

    @search_account
    def active_account(self, id, status = 0):
        """
        a function to activate an account, 
        receive the account id
        """
        if status == 1:
            self.__accounts[id]['account'] = True
            return f"el id {id} a sido activado"
        elif status == 0:
            return f"el id {id} ya estaba activa"
        return f"el id {id} no exite en el banco"

        
    def get_account(self):
        return self.__accounts

bnb = bank()
print(bnb.active_account('0021'))
print(bnb.get_account())

#%%
"""
decorators to see if a loan can 
be given or not to a client
"""

accounts_bank = {
    '001': {'name': 'Juan', 'ci':111, 'account': True,   
            'borrow': {'amount': 1000, 'paid_out': 800},
    },
    '002': {'name': 'Pedro', 'ci':222, 'account': True, 
        'borrow': {'amount': 2000, 'paid_out': 100},
    },
    '003': {'name': 'Maria', 'ci':333, 'account': True, 
        'borrow': {'amount': 5000, 'paid_out': 2800},
    },
}

government_data = {
    111: {'name': 'Juan', 'age': 20, 'income': 3000},
    222: {'name': 'Pedro', 'age': 30, 'income': 4000},
    333: {'name': 'Maria', 'age': 40, 'income': 8000},
}

def check_government_data(origin_func):
    def envolt(self, *args, **kwargs):
        if args[0] in government_data:
            return origin_func(self, args, government_data[args[0]]['income'])
        return origin_func(self, args[0], credit = False)
    return envolt

def check_bank_account(origin_func):
    def envolt(self, *args, **kwargs):
        person = {}
        amount = args[0][1] #monto del prestamo
        salary = args[1] #salario del cliente
        for i in self.get_account():
            if self.get_account()[i]['ci'] == args[0][0]:
                person = accounts_bank[i]
                new_amount = amount + (person['borrow']['amount'] - person['borrow']['paid_out']) 
                if new_amount < 3 * salary:
                    self.get_account()[i]['borrow']['amount'] = new_amount
                    return origin_func(self, args[0][0], new_amount, credit = True)
                return origin_func(self, args[0][0], new_amount, credit = False)
    return envolt

class bank:
    __accounts = None

    def __init__(self, accounts) -> None:
        self.__accounts = accounts
    
    @check_government_data
    @check_bank_account
    def to_lend(self, ci, amount, credit = True):
        if credit:
            return f'Snr {ci} su credito de {amount} fue aprobado'
        return f'Snr {ci}su credito de {amount} fue rechazado'

    def get_account(self):
        return self.__accounts

bnb = bank(accounts_bank)
print(bnb.to_lend(111, 1000))
print(5*"*")
print(bnb.get_account())

#%%
def k(g):
    def h(x):
        print('k')
        return g(x) ** 2
    return h

def g(f):
    def h(x):
        print('g')
        return f(x) * 2
    return h

@k
@g
def f(x):
    return x + 1

print(f(3))
# %%
