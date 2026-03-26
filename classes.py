from rich import *

class Produto:
    def __init__(self,nome, preco, quantidade):
        self.nome = nome
        self.preco = float(preco)
        self.quantidade = int(quantidade)
        self.id_produto = None
        
    def __str__(self):  # Novo método para representação legível
        return f'ID: {self.id_produto},\nProduto: {self.nome},\nPreço: {self.preco},\nQuantidade: {self.quantidade}'

    def __repr__(self):  # É usado quando Python precisa representar objetos em listas
        return self.__str__()

class CarrinhoDeCompras:

    def __init__(self):
        self.lista_carrinho = [] #composição
        self.proximo_id = 1

    def adicionar_produto(self, produto):
        id = self.gerar_id()
        produto.id_produto = id
        self.lista_carrinho.append(produto)

    def gerar_id(self):
        # Implementação simplificada para geração de ID
        id_atual = self.proximo_id #Variavel para armazenar os id ja gerados 
        self.proximo_id += 1 # Gera o proximo id, realizando a soma de acordo com o anterior
        return id_atual

    def remover_produto(self,id_remover):
        encontrou = False
        for produto in self.lista_carrinho:
            if produto.id_produto == id_remover:
                self.lista_carrinho.remove(produto)
                print('[green]Produto removido do carrinho[/]')
                encontrou = True
                return
                
        if encontrou == False:
                print('[red]Nenhum produto no seu carrinho possui esse id')

    def listar_produto(self):
        for produto in self.lista_carrinho:
            print(f'ID: {produto.id_produto}, Produto: {produto.nome}, Valor: {produto.preco}, quantidade: {produto.quantidade}')
    
    def calcular_total(self):
        valor_total = 0
        for produto in self.lista_carrinho:
            valorproduto = produto.preco * produto.quantidade
            valor_total += valorproduto
        print(valor_total)

    def buscar_produto(self, nome):
        encontrou = False
        for produto in self.lista_carrinho:
            if produto.nome == nome:
                print('[green]Produto encontrado![/]')
                print(f'ID: {produto.id_produto}, Produto: {produto.nome}, Valor: {produto.preco}, quantidade: {produto.quantidade}')
                encontrou = True
                return
        if not encontrou:
            print(f'[red]O produto {nome} não esta disponivel no momento![/]')

class Pedido:
    def __init__(self,carrinho):
        self.carrinho = carrinho #agregação

    def gerar_pedido(self):
        for produto in self.carrinho.lista_carrinho:
            print(f'Produto: {produto.nome}\n'
                  f'Valor unitario: {produto.preco}\n'
                  f'Quantidade: {produto.quantidade}\n'
                  f'valoe total: {self.carrinho.calcular_total}')
    
    def mostrar_produto(self):
        pass

    def exibir_total(self):
        pass