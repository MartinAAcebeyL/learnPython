import mysql.connector
from Lib_py_para_principiantes_dev import function 


def palindromo(sentencia):
    str(sentencia).lower()
    #sentencia = str(sentencia).replace(" ","")
    print(sentencia)

if __name__ == "__main__":
    palindromo("holaAOPreW")
