'''def valida_int (pergunta,min,max):
    while (x < min) or (x > max):
        x = int(input(pergunta))
    return x



def fatorial (num):
    
    fat = 1
    if num == 0:
        return fat
    for i in range (1,num + 1 ,1):
        fat *= i
    return fat

x = valida_int('Digite um número inteiro:',0,9999)
print(f'{x}! = {fatorial(x)}')

-----------------------------------------------------------------------------------------------------------------------------------------------------------------'''
def existeArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')
        a.close()
    except :
        print('Erro na criação do Arquivo!')
    else:
        print(f'Arquivo {nomeArquivo} criado com sucesso"')

def valida_int (pergunta, min, max):
    x = int(input(pergunta))
    while (x < min) or (x > max):
        print('\nNúmero inexixtente, selecione um número do menu!\n')
        print('       Menu\n')
        print('1 - Cadastrar novo Item')
        print('2 - Listar Cadastros')
        print('3 - Sair\n')
        x = int(input(pergunta))
    return x

def cadastrarJogo(nomeArquivo, nomeJogo, Nomevideogame):
    try:
        a = open(nomeArquivo, 'at')
    except:
        print('Erro ao Cadastrar Jogo!')
    else:
        a.write(f'{nomeJogo}; {nomeVideogame}\n')
        print('Jogo cadastrado!')
    finally:
        a.close()

def listarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
    except:
        print(f'Falha ao Listar os Itens do Arquivo {nomeArquivo}')
    else:
        print(a.read())
    finally:
        a.close()



# Programa Principal
arquivo = 'games.txt'
if existeArquivo(arquivo):
    print('Arquivo localizado no computador!')
else:
    print('Arquivo Inexistente!')
    criarArquivo(arquivo)

while True:
    print('       Menu\n')
    print('1 - Cadastrar novo Item')
    print('2 - Listar Cadastros')
    print('3 - Sair\n')

    op = valida_int('Escolha a Opção Desejada: ', 1, 3)

    if op == 1:
        print('Opção de Cadastro selecionada:\n')
        nomeJogo = input('Nome do Jogo: ')
        nomeVideogame = input('Nome do Video Game; ')
        cadastrarJogo(arquivo, nomeJogo, nomeVideogame)

    elif op == 2:
        print('Lista de Cadastros:\n')
        listarArquivo(arquivo)
    else:
        print('\nEncerrando programa...\n')
        break


