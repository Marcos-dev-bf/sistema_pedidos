class Produto:
    def __init__(self,nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade


class Carrinho:

    def __init__(self):
        lista_carrinho = [] #composição

    def adicionar_produto(self, produto):
        
        print(produto.nome)

    def gerar_id(self):

        return

    def remover_produto(self):
        pass
    
    def listar_produto(self):
        pass
    
    def calcular_total(self):
        pass

    def buscar_produto(self):
        pass
    pass

class Pedido:
    def gerar_resumo(self):
        pass
    
    def mostrar_produto(self):
        pass

    def exibir_total(self):
        pass
    pass