#Aula 12 : Loop For

"""carros=["HRV","Golf","Argo","Focus","Fit","Fusion","Polo"]

for x in carros:
    print(x)
    if(x=="Fit"):
        break
    
print("Fim do Programa")"""

#Aula 13: Função Input

"""nome=input("Digite Seu Nome")
print(f"nome digitado: {nome}")"""

"""import os
os.system('cls')

num1=int(input("Digite o Primeiro Valor.:"))
num2=int(input("Digite o Segundo Valor:.."))
res=num1+num2
print(f'Soma dos Valores: {res}')"""

#Aula:14 Loop While

"""inicialização de variável de controle
while(teste lógico)
    comando1
    comando2
    comandoX
    inc ou dec ou controle """


"""carros=["HRV","Golf","Argo","Onix","Focus"]
i=0
tam=len(carros)
while i<tam:
    print(carros[i])
    i+=1 # ou i=i+1

print("Fim do Loop")
print(tam)"""

"""import os

carros=[]
carro=input('Digite o nome do novo carro: ')

while carro!= '-1':
    carros.append(carro)
    carro=input('Digite o nome do novo carro: ')

os.system('Cls')

for x in carros:
    print(x)

print('\nFim do Loop')"""

#Aula 15: Tuplas

"""t_carros=("HRV","Golf","Argo")

l_carros=list(t_carros)
l_carros[2]="Focus"

t_carros=tuple(l_carros)

for x in t_carros:
    print(x)"""

#Aula 16: Matrizes

"""carros=[["Modelo","HRV"],["Fabricante","Honda"],["Ano",2016]]

carros[2][1]=2019
carros.append(["Cor","Prata"])

for l,c in carros:
    print(f"Linha: {l} | Coluna: {c}")"""

#Aula17: Dictionary

#Key:Value   sempre nesta ordem

"""carro={
    "Carro1":{
        "Fabricante":"Honda",
        "Modelo":"HRV",
        "Ano":"2016",
        "Cor":"Prata"
    },
    "Carro2":{
        "Fabricante":"Volksvagem",
        "Modelo":"Golf",
        "Ano":"2019",
        "Cor":"Preto"
        },
    "Carro3":{
        "Fabricante":"Ford",
        "Modelo":"Focus",
        "Ano":"2021",
        "Cor":"Branco"
        }
}
"""
"""fab=carro["Fabricante"] #fab=carro.get("Fabricante")

carro["Cambio"]="Automatico"
carro.pop("Cambio") #del carro ["Cambio"]
carro.clear #Limpa tudo


print(f"Tamanho do Dictionary: {len(carro)}")"""

"""for x in carro:
    print(x) #chave
    print(carro[x]) #valor"""

"""for c,v in carro.items ():
    print(f"{c} : {v}")"""

#print(carro["Carro1"]["Fabricante"])

"""Carro1={
    "Fabricante":"Honda",
    "Modelo":"HRV",
    "Ano":"2016",
    "Cor":"Prata"
},
Carro2={
    "Fabricante":"Volksvagem",
    "Modelo":"Golf",
    "Ano":"2019",
    "Cor":"Preto"
},
Carro3={
    "Fabricante":"Ford",
    "Modelo":"Focus",
    "Ano":"2021",
    "Cor":"Branco"
}

carros={"Carro1":Carro1,"Carro2":Carro2,"Carro3":Carro3}

print(carros["Carro1"])"""

#Aula18: Jogo de Advinhação

"""import random
import os

erros=0
sorteado=random.randrange(0,100)
jogador=int(input("Digite seu Número: "))

while(sorteado !=jogador):
    os.system('cls')
    if(sorteado>jogador):
        print("Erro, o número é maior")
    elif(sorteado<jogador):
        print("Erro, o número é menor")
    erros+=1
    jogador=int(input("Digite Novamente seu Número:"))
print(f"Número {jogador}, você acertou em {erros+1} tentativas")"""