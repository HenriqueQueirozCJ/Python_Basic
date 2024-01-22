#       01345678910
import os
nome = "Henrique"

indice = 0
novo_nome = ''

while indice < len(nome):
    letra = nome[indice]
    novo_nome += "*" + letra 
    indice += 1
os.system("clear")
print(f'\n {novo_nome}')
