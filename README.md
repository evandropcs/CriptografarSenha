# CriptografarSenha

CriptografarSenha_vs1:

#### CRIPTOGRAFIA

1) Gera letras aleatorias.
2) Criptografa a senha (strig) colocando a senha dentro de uma lista chadama cripto, e acrescenta letras aleatórias antes e depois de cada caracter da senha original.

#### DECRIPTOGRAFIA

1) Decriptografa através do fatiamento da lista cripto, e depois junta todos os caracteres. 


CriptografarSenha_vs2:

#### CRIPTOGRAFIA

1) Cria um laço de repetição que percorre cada caracter da senha.
2) Criptografa a senha:
3) Transforma cada caracter da senha em um numero (inteiro + 1034) atraves da função ORD.
4) Transforma cada inteiro retornado pela função ORD em unicode através da função CHR.
5) Retorna a senha criptografada.

#### DECRIPTOGRAFIA

1) Cria um laço de repetição que percorre cada caracter da senha criptografada.
2) Criptografa a senha:
3) Transforma cada caracter da senha em um numero (inteiro - 1034) atraves da função ORD.
4) Transforma cada inteiro retornado pela função ORD em unicode através da função CHR.
5) Retorna a senha decriptografada.
