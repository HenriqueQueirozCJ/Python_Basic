"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
'''num = input("Digite um numero inteiro: ")

try:
    num = int(num)
    if (num % 2 ==0):
        print("O número digitado é par !")
    else:
        print("O número digitado é ímpar! ")
except:
    print("Digite somente números inteiros !")'''

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = int(input("Informe a hora atual sem os minutos: "))
if(hora <= 11):
    print("Bom dia !")
elif(hora >=12 and hora <=17):
    print("Boa tarde !")
else:
    print("Boa noite !")   

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

'''nome = input("Digite seu nome: ")

if(len(nome)<=4):
    print("Seu nome é curto! ")
elif(len(nome)>=5 and len(nome) <= 6):
    print("Seu nome é normal")
else:
    print("Seu nome é muito grande! ")'''