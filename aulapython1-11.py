#Aula 1 : Print

"""canal="Curso de "
curso="Python"
print(canal + curso)"""

#Aula 2: Sintaxe Básica

"""if 10 < 2:
 print("maior")
 print("aula2")
print("fim")"""



"""num1=num2=res=0
def cn():
  global canal
  canal ="Jhonatan"
cn()
print(canal)"""

#AUla 3: Variáveis 

"""y=["Carro","Avião", "Navio"] #List / Array
x=("Carro","Avião", "Navio") #Tupla (não modifica itens como no array)
y[1]= "Onibus"
z=range(0,100,1) #List

print(f"Valor: + {z}")
print(f"Tipo: + {type(z)}")"""

#Aula 4: Tipos de Dados

"""x={
    "canal":"CFB Cursos",
    "curso":"Curso de Python",
    "nome": "Bruno"
}
print(f"Valor: + {x["canal"]}")
print(f"Tipo: + {type(x)}")"""



"""x={5,7,4,5,7,4,8} #Set
x=frozenset({5,7,4,5,7,4,8}) #Set
print(f"Valor: + {x}")
print(f"Tipo: + {type(x)}")"""

#Aula 5:Tipo Numéricos

"""import random
num_i=10
num_f=5.2
num_c=1j
num_r=[
random.randrange(0,10),
random.randrange(10,20),
random.randrange(20,30),
random.randrange(30,40),
random.randrange(40,50),
random.randrange(50,60)]

x=num_r

print(f'Valor 1: {x[0]} - Tipo: {type(x[0])}')
print(f'Valor 2: {x[1]} - Tipo: {type(x[1])}')
print(f'Valor 3: {x[2]} - Tipo: {type(x[2])}')
print(f'Valor 4: {x[3]} - Tipo: {type(x[3])}')
print(f'Valor 5: {x[4]} - Tipo: {type(x[4])}')
print(f'Valor 6: {x[5]} - Tipo: {type(x[5])}')"""

#Aula 6 e 7: Strings P1 e P2

"""curso='Curso de Python'
canal='CFB Cursos'
palavra='python'

#print(curso[0:5])
#print(curso.strip())
#print(curso.lower().strip())
#print(curso.upper())
#print(curso.replace('Python','C#'))
#print(curso.split(' '))
#print(f'Tamanho: {len(curso)}')

res=palavra.upper() in curso.upper()
print(res)

res=curso+' do canal '+canal
print(res)"""

"""cidade='Campinas'
dia=19
mes='Fevereiro'
ano=2026
canal='CFB Cursos'

print(f'{cidade}, {dia} de {mes} de {ano}\r{canal} ')"""

"""\' = imprimir aspas simples
\" = imprimir aspas duplas
\n = quebra de linha
\r = retorno de carriage (volta ao inicio da linha atual)
\t = tabulação (tab)
\b = backspace (apagar o caracter anterior)"""

#Aula 8: Tipo Boolean

"""aula=10<15

print(bool(aula)) #True or False"""

#Aula 9: Coleção List

"""carros=["HRV","Golf","Argo","Focus"]
carros.append('Fit')
carros.append('Fusion')
carros.append('Polo') #adiciona um valor
carros.remove('Fusion') #remove apenas por valor
carros.pop() #remove o ultimo e pode mostrar o valor que removeu
del carros[2] #remove por indice
#carros.clear()

carros2=list(carros) #copiar
carros3=["Fusca","147","Brasilia","Celta"]
carros4=carros+carros3
carros4.remove([2])

print(len(carros4))
print(carros4)"""

#Aula 10: Como usar o If

"""a=10
b=5
op='/'
res=0

if op=='+':
    res=a+b
elif op=='-':
    res=a-b
elif op=='*':
    res=a*b
elif op=='/':
    res=a/b
else:
    print("Operador Inválido")

print(f'{a}{op}{b}={res}')"""

#Aula 11: Condicionar If Elif Else

"""clima='Sol'
dinheiro=600
lugar=''

if clima=='Sol' and (300 <= dinheiro <= 500):
    lugar='Clube'
else:
    lugar='Cinema'

print("Vou ao "+ lugar)"""