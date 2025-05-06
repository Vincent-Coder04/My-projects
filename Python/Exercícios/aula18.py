class Pessoa:
   def __init__(self, nome, idade):
      self.nome = nome
      self.idade = idade 
      
   def apresentar(self):
      print(f"Olá, meu nome é{self.nome} e tenho {self.idade} anos.")

p1 = Pessoa("tralalelo", 10000)
p2 = Pessoa("bombardino", 12) 
p1.apresentar()
p2.apresentar()
