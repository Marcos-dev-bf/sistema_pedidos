from rich import *
from classes import *

def leia_int(mensagem):
    while True:
        try:
            usuario = int(input(mensagem))
            return usuario
        
        except ValueError:
            print('Digite corretamente')

def leia_float(mensagem):
    while True:
        try:
            usuario = float(input(mensagem))
            return usuario
        
        except ValueError:
            print('[red]Erro[/]')

def leia_string(mensagem):
    while True:
        try:
            usuario = str(input(mensagem))
            return usuario
        
        except ValueError:
            print('[red]Erro[/]')
def primeiras_opcoes():
    lista = ['Adicionar produto', 'Remover por ID', 'Listar produtos','Calcular total', 'Buscar produto', 'Finalizar pedido']
    for numero, acao in enumerate(lista):
        print(f'{numero+1} = {acao}')

def segundas_opcoes():
    lista = ['Voltar ao menu principal']
    for numero, acao in enumerate(lista):
        print(f'{numero+1} = {acao}')

def selecionar_opcao():
    usuario = leia_int('Digite a ação que deseja realizar: ')
    carrinho = CarrinhoDeCompras()
    if usuario == 1: #adicionar produto

        while True:
            nome_produto = leia_string('Nome do produto: ')
            valor_produto = leia_float('Valor produto')
            quantidade_produto = leia_int('Digite a quantidade: ')
            c1 = Produto(nome_produto,valor_produto,quantidade_produto)
            carrinho.adicionar_produto(c1)

            continua = leia_int('Deseja continuar?\n[1] = Não\n[2] = Sim\nDeseja continuar? ')
            if continua == 1:
                break
            elif usuario > 2:
                print('Opão invalida, digite umas das opçoes disponiveis!')
    elif usuario == 2:
        while True:
            remover = leia_int('Digite o id que deseja remover: ')
            carrinho.remover_produto(remover)
            continua = leia_int('Deseja continuar?\n[1] = Não\n[2] = Sim\nDeseja continuar? ')
            if continua == 1:
                break
            elif usuario > 2:
                print('Opão invalida, digite umas das opçoes disponiveis!')

    elif usuario == 3:
        carrinho.listar_produto()
    
    elif usuario == 4:
        total = carrinho.calcular_total()
        if total == 0:
            print('Valor esta zerado!')

    elif usuario == 5:
        produto_procurado = leia_string('Qual produto deseja procurar: ')
        carrinho.buscar_produto(produto_procurado)
