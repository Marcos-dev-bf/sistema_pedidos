from classes import *
from Funcoes import *

print
c1 = Produto("Coca-cola", 5.00, 10)
c2 = Produto("Pepsi", 4.50, 8) 
carrinho = Carrinho()
carrinho.adicionar_produto(c1) 
carrinho.adicionar_produto(c2)
print(carrinho.gerar_id())
