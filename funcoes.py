import sys

def buscaindice(nome):
    database = ["Adelmo", 5722.50, 22, "Marcos", 32.890, 19, "Cilso", 68893.75, 2, "Aline", 4000, 20, "Airan",
    32278.02, 20, "Josiane Igor", 19210.44, 19, "Siley Pastor", 12806.96, 27, "Rose Marco", 16.785, 4,
    "Jonatas Evangelista", 8523.86, 1]
    if nome in database:
        client = database.index(nome)
        carteira = database[client+1]
        dia = database[client+2]
        return carteira, dia
    else:
        print("Nome incorreto!")
        print("Verifique a lista e rode o programa novamente!")
        sys.exit()

def rendimento(carteira,porcentagem):
    lucro = carteira * (porcentagem/100)
    return lucro
        
def taxanxt(lucro, taxa):
    desconto =lucro * (taxa/100)
    return desconto

def afterretirada(a,b,c):
    saldobruto = a + b - c
    return saldobruto

def beforeretirada(a,b):
    retirada = a - b
    return retirada
