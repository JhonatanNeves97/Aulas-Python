from datetime import datetime

cadastro = {'nome':[],'ano':[],'sexo':[]}
total = 0
total_idade = 0
hoje = datetime.now().year
while True:

    terminar = input('Deseja cadastrar uma pessoa? [S/N]:')
    if terminar.upper() == 'N':
        break
    if terminar.upper() not in ("S","N"):
        print('Digite "S" para SIM e "N" para NÃO')
        continue

    nome = input('Qual o nome? ')
    ano = int(input('Qual o ano de nascimento? '))
    sexo = input('Qual o sexo? ')

    cadastro['nome'].append(nome)
    cadastro['ano'].append(ano)
    cadastro['sexo'].append(sexo.upper())

    total +=1
    total_idade += hoje - ano

media = total_idade/total

print(cadastro)
print(f'Total de cadastros:{total}')
print(f'Média de idade das pessoas é: {media}')

print('Mulheres acima de 30 anos')
for i in range(len(cadastro['nome'])):
    idade = hoje - cadastro['ano'][i]
    if cadastro['sexo'][i] == 'F' and idade > 30:
        print(cadastro['nome'][i], idade)

print('Homens acima da média')
for i in range(len(cadastro['nome'])):
    idade = hoje - cadastro['ano'][i]
    if cadastro['sexo'][i] == 'M' and idade > media:
        print(cadastro['nome'][i], idade)





