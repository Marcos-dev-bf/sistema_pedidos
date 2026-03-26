from classes import *
from Funcoes import *


carrinho = CarrinhoDeCompras()
c1 = Produto("Coca-cola", 5.00, 10)
carrinho.adicionar_produto(c1) 
c1 = Produto("Pepsi", 4.50, 8) 
carrinho.adicionar_produto(c1)
carrinho.listar_produto()
usuario = int(input('Digite o id que deseja remover: '))
carrinho.remover_produto(usuario)
carrinho.listar_produto()
carrinho.calcular_total()
carrinho.buscar_produto('Coca-cola')

pedido = Pedido(carrinho)
pedido.gerar_pedido()