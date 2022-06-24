def criptografar(senha: str):
    senha_cripto = ''
    for x in senha:
        # CHR recebe um inteiro entre 0 a 1.114.111, retorna um unicode
        # ORD recebe um unico unicode e retorna um inteiro
        senha_cripto += chr(ord(x)+1034)
    return senha_cripto


def decriptografar(senha):
    senha_decripto = ''
    for x in senha:
        # CHR recebe um inteiro entre 0 a 1.114.111, retorna um unicode
        # ORD recebe um unico unicode e retorna um inteiro
        senha_decripto += chr(ord(x)-1034)
    return senha_decripto


# Criptografa o senha 'T9x8v23NB@' e mostra na tela a senha criptografada.
print(criptografar('T9x8v23NB@'))

# Decriptografa 'ўу҂тҀмнјьъ' e mostra na tela a senha.
print(decriptografar('ўу҂тҀмнјьъ'))


