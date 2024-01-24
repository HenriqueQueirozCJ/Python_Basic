"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""

lista = ['Maria','Helena','Luiz']
i=0

indices = range(len(lista))
print(indices)

for indice in indices:
    print(indice, lista[indice])