class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def aplicar_desconto(self, porcentagem):
        desconto = self.preco * (porcentagem/100)
        self.preco -= desconto 

    def mostrar_produto(self):
        print(f"{self.nome} custa R$ {self.preco:.2f}")

produto = Produto("Monitor", 1200)
produto.mostrar_produto()
produto.aplicar_desconto(10)
produto.mostrar_produto()

