"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""
while True:
    nome = input("Digite seu nome: ")
    idade = input("Informe sua idade ")

    if nome and idade:

        print(f'Seu nome é {nome}',f'\nSeu nome invertido é {nome[::-1]}')
        print(f'Seu nome contém {len(" ")} espaços')
        print(f'Seu nome contém {len(nome)} letras',f'\nE a última letra do seu nome é : {nome[-1]}')
        break
    else:
        print("Não deixe o espaço em branco !")
    continue