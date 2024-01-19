'''print(1234)
print(456)

int('a')'''

'''while True:'''
abc = input("Digite um número:  ")

'''if (abc.isdigit()):
        print(f"O número é: {abc}")
        break
    else:
        print(f'Digite somente números')
    continue'''

try:
    abc_2 = float(abc)
    print(f'O número é: {abc_2}')
except:
    print(f'Digite somente números')
