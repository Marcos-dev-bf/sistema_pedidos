class Produto:
    def __init__(self,nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.id_produto = None


class Carrinho:

    def __init__(self):
        lista_carrinho = [] #composição

    def adicionar_produto(self, produto):
        id = self.gerar_id()
        produto.id_produto = id
        self.lista_carrinho.append(produto)

    def gerar_id(self):
        # Implementação simplificada para geração de ID
        proximo_id =+ 1 
        return proximo_id

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