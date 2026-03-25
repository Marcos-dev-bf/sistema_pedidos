class Produto:
    def __init__(self,nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.id_produto = None


class Carrinho:

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

    def remover_produto(self):
        for produto in self.lista_carrinho:
            print(f'ID: {produto.id_produto}, Produto: {produto.nome}, Valor: {produto.preco}, quantidade: {produto.quantidade}')
    
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