import os
frase ="Lorem ipsum dolor sit amet, \
consectetur adipiscing elit. Nam aliquam sollicitudin nisl, vel ullamcorper eros ornare ut.\
 Donec molestie tristique velit eu mollis. Aliquam vitae elit diam. \
    Donec ac neque vel nisl volutpat imperdiet. Etiam non diam a odio fermentum luctus"
    
i = 0
qtd_apareceu_mais_vezes = 0
letra_que_apareceu_mais_vezes = ' '

while i < len(frase):

    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    letra_que_mais_apareceu = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < letra_que_mais_apareceu:
        qtd_apareceu_mais_vezes = letra_que_mais_apareceu
        letra_que_apareceu_mais_vezes = letra_atual
    i+=1

os.system("clear")

print(
    "A letra que mais apareceu foi o "
      f'{letra_que_apareceu_mais_vezes} que apareceu '  
      f'{qtd_apareceu_mais_vezes}x'
)