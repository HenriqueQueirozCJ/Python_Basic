a = float(input("Digite qualquer número: "))
b = float(input("Digite qualquer número: "))
c = float(input("Digite qualquer número: "))

adicao = a + b + c
subtracao = a - b - c
multiplicacao = a * b * c
divisao = (a + b + c) /3

if(a>b and a>c):{
    print(f'{a:.1f} é maior que {b:.1f} e maior que {c:.1f}')
}
elif(b>a and b>c):{
    print(f'{b:.1f} é maior que {a:.1f} e maior que {c:.1f}')
}
else:{
    print(f'{c:.1f} é maior que {b:.1f} e maior que {a:.1f}')
}
    
print(f'A soma de {a} + {b} + {c} = {adicao}',
      f'\nA subtração de {a} - {b} - {c} = {subtracao}',
      f'\nA multiplicação de {a} * {b} * {c} = {multiplicacao}',   
      f'\nA divisao de {a} + {b} + {c} / 3 = {divisao}')