'''Aula 4'''

'''i = 3

while (i<13):
    print(i)
    i+=1

for i in range (3,13,1):
    print(i)

i=0
while (i<9):
    print (i)
    i+=2

for i in range(0,9,2):
    print(i)

    

print('Lanchonete')
print('1 - Coxinha R$ 5,00')
print('2 - Pastel R$ 7,00')
print('3 - Café R$ 4,00')
print('4 - Suco R$ 6,00')
print('5 - Sair')

total = 0

while True:
    op = int(input("Qual Item gostaria de comprar? "))
   
    
    if (op == 1):
        qtd = int(input("Quantas unidades quer comprar? "))
        total = total + qtd * 5
    elif (op == 2):
        qtd = int(input("Quantas unidades quer comprar? "))
        total = total + qtd * 7
    elif (op == 3):
        qtd = int(input("Quantas unidades quer comprar? "))
        total = total + qtd * 4
    elif (op == 4):
        qtd = int(input("Quantas unidades quer comprar? "))
        total = total + qtd * 6
    elif (op == 5):
        break
    else: 
        print("Produto Inválido, selecione outro!")
print(f'Você Gastou um total de R$ {total}')



valor = int(input('Digite o Valor em Reais: '))

while True:
    if valor >= 100:
        cont100 = valor // 100
        valor = valor - cont100 * 100
        print (f'Cédulas de 100: {cont100}')
        if not valor:
            break

    if valor >= 50:
        cont50 = valor // 50
        valor = valor - cont50 * 50
        print (f'Cédulas de 50: {cont50}')
        if not valor:
            break

    if valor >= 20:
        cont20 = valor // 20
        valor = valor - cont20 * 20
        print (f'Cédulas de 20: {cont20}')
        if not valor:
            break

    if valor >= 10:
        cont10 = valor // 10
        valor = valor - cont10 * 10
        print (f'Cédulas de 10: {cont10}')
        if not valor:
            break

    if valor >= 5:
        cont5 = valor // 5
        valor = valor - cont5 * 5
        print (f'Cédulas de 5: {cont5}')
        if not valor:
            break

    if valor >= 2:
        cont2 = valor // 2
        valor = valor - cont2 * 2
        print (f'Cédulas de 2: {cont2}')
        if not valor:
            break

    if valor:
        cont1 = valor 
        print (f'Cédulas de 1: {cont1}')
        break'''




dinheiro = 0
pessoa = 0
soma_idade = 0
print('Valores dos Ingressos:\n Menor de 3 anos - Gratuito \n De 3 a 12 anos R$ 15,00 \n Mais de 12 anos R$ 30,00')
print('Digite 0 para sair')

while True:
    idade = (int(input('Digite a Idade da Pessoa: ')))
    if idade == 0:
        break

    pessoa += 1
    soma_idade += idade

    if (idade < 3 ):
        dinheiro += 0
    elif (idade > 12):
        dinheiro += 30
    else:
        dinheiro += 15

if dinheiro > 0 :
    media = soma_idade // pessoa

    print(f'Total de Pessoas: {pessoa}')
    print(f'Total de dinheiro gasto: {dinheiro}')
    print(f'Média de Idade: {media}')
       

