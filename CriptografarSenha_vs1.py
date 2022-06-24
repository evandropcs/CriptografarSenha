# Gera letras aleatorias
def aleatoria(qtd):
    import random
    import string
    aleatorias = (random.sample(string.ascii_letters, qtd))
    return aleatorias


def criptografar(senha: str):
    lista = list(senha)
    cripto = []
    for letra in lista:
        aleatorias = aleatoria(4)
        cripto += aleatorias
        cripto += letra
        aleatorias = aleatoria(4)
        cripto += aleatorias
    return cripto


def decriptografar(cripto):
    senha = cripto[4::9]
    senha = ''.join(senha)
    return senha


# Criptografa a senha 'T9x8v23NB@' e armazena o resultado na variavel senha_cripto.
texto_cripto = criptografar('T9x8v23NB@')

# Mostra na tela a senha criptografada.
print(texto_cripto)

# Decriptografa 'ўу҂тҀмнјьъ' e mostra na tela a senha.
print(decriptografar(texto_cripto))


