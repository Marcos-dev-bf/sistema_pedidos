from classes import *
from Funcoes import *


c1 = Produto("Coca-cola", 5.00, 10)
c1 = Produto("Pepsi", 4.50, 8) 
carrinho = Carrinho()
carrinho.adicionar_produto(c1) 
carrinho.adicionar_produto(c1)

carrinho.remover_produto()
