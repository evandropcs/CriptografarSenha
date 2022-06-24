# Gera letras aleatorias
def aleatoria(qtd):
    import random
    import string
    aleatorias = (random.sample(string.ascii_letters, qtd))
    return aleatorias

# Criptografa o texto escolhido
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

# Decriptografa o texto
def descriptografar(cripto):
    senha = cripto[4::9]
    senha = ''.join(senha)
    return senha

# Recebe o texto do usuário
palavra = input('Escolha uma palavra para ser criptografada: ')

# Chama as funções
cripto = criptografar(palavra)
descripto = descriptografar(cripto)

# Mostra na tela texto criptofrado e decriptografado
print(f'A palavra criptografada é: {cripto}')
print(f'A palavra criptografada é: {descripto}')

