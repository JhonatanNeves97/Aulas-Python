'''maca = 2.30
banana = 1.85
laranja = 3.60
total = 0

produto = int(input('Digite qual produto deseja comprar \n 1 para maçã \n 2 para banana \n 3 para laranja \n Qual deseja comprar?: '))
quantidade = int(input('Digite quantas unidades deseja comprar: '))

if produto == 1:
    total = maca * quantidade
    print(f'Você comprou {quantidade} maçã(s) por {total:.2f}')
elif produto == 2: 
    total=banana*quantidade
    print(f'Você comprou {quantidade} banana(s) por {total:.2f}')
elif produto == 3:
    total=laranja*quantidade
    print(f'Você comprou {quantidade} laranja(s) por {total:.2f}')
else:
    print('Você digitou o número errado')'''



'''lado1 = int(input('Digite o primeiro lado do triângulo: '))
lado2 = int(input('Digite o segundo lado do triângulo: '))
lado3 = int(input('Digite o terceiro lado do triângulo: '))

if lado1 == 0 or lado2 == 0 or lado3 == 0:
    print('Nenhum lado pode ser igual a 0!')
elif lado1 > lado2 + lado3 or lado2 > lado1 + lado3 or lado3 > lado1 + lado2:
    print ('Um lado nao pode ser maior que a soma dos outros 2 lados!')
else:
    if lado1 == lado2 == lado3:
        print('Seu triângulo é Equilátero!')
    elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
        print('Seu triângulo é Escaleno!')
    else:
        print('Seu triângulo é Isóceles!')'''
              
kwh = 300
tipo = 'c'

if tipo == 'R':
    if kwh >= 500:
        preco = 0.65
    else:
        preco = 0.4
    print(f'total a pagar: {kwh * preco}')




