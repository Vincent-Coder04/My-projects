'''
1. (Conceitual)
O que é um atributo em uma classe Python?
A) Uma função especial = X
B) Uma variável que pertence a um objeto = ✅ 
C) Uma estrutura de repetição interna = X
D) Um parâmetro usado fora do __init__ = X
'''
'''
2. (Conceitual)
Qual a diferença entre método e função comum em Python?
A) Não há diferença = X
B) Método sempre retorna True = X
C) Método é uma função definida dentro de uma classe e acessa atributos via self = ✅ 
D) Função tem self, método não = X
'''
'''
3. (Código - Interpretação)
O que esse código imprime?
R:Olá, Lucas!
'''
class Pessoa:
 def __init__(self, nome):
    self.nome = nome
 def saudacao(self):
    print(f"Olá, {self.nome}!")
p = Pessoa("Lucas")
p.saudacao()
'''
4. (Prática)
O que acontece se você tentar acessar um atributo que não existe em um objeto?
A) O Python ignora e segue o código = X
B) Ele cria o atributo automaticamente = X
C) Ocorre um erro: AttributeError = ✅
D) O atributo é definido como None = X
'''
'''
5. (Código - Completar)
Complete o método abaixo para que ele imprima a idade do aluno:
'''
class Aluno:
 def __init__(self, nome, idade):
  self.nome = nome
  self.idade = idade
 def mostrar_tudinho(self):
  print(f"O nome do ser humaninho é {self.nome} e a idade dele é {self.idade}")

p = Aluno("Chicken Jockey", 200)
p.mostrar_tudinho()
'''
6. (Código - Análise de erro)
Qual o erro no código abaixo?
class Produto:
def __init__(self, nome, preco):
self.nome = nome
self.preco = preco
def mostrar():
print(f&quot;{self.nome} custa R${self.preco}&quot;)
A) Faltou ponto e vírgula = X
B) O método mostrar() não recebe self = ✅
C) Atributos estão errados = X
D) print deveria estar fora da classe = X
'''
'''
7. (Criação de método personalizado)
Crie um método chamado desconto() dentro de uma classe Produto que reduza o
preço em 10%.
'''
class Produto:
    def __init__(self, valor):
        self.valor = valor
        self.descontao = 0

    def desconto(self):
        descontinho = self.valor * 0.10
        self.descontao = self.valor - descontinho

    def chickenjockey(self):
        print(f"O valor inicial é {self.valor}, com o valor do desconto fica {self.descontao:.2f}")

v1 = Produto(100)
v1.desconto()
v1.chickenjockey()
'''
8. (Conceitual)
O que o método especial __init__ faz?
A) Remove atributos do objeto = X
B) É o construtor da classe, chamado na criação do objeto = ✅
C) Serve apenas para criar métodos = X
D) Executa o método principal do Python = X
'''
'''
9. (Código com método que retorna valor)
Qual a saída do código?
class Circulo:
def __init__(self, raio):
self.raio = raio
def area(self):
return 3.14 * (self.raio ** 2)
c = Circulo(2)
print(c.area())
'''
class Circulo:
 def __init__(self, raio):
  self.raio = raio

 def area(self):
  return 3.14 * (self.raio ** 2)

c = Circulo(2)
print(c.area())
'''
10. (Reflexiva/aberta)
Explique com suas palavras a diferença entre um atributo e um método.
Dê um exemplo de cada dentro de uma mesma classe.
R: Atributos são variáveis ligadas a um objeto, que guardam suas características. Métodos são funções dentro da classe que trabalham com esses atributos, podendo mostrar, alterar ou usar esses valores de alguma forma.
Exemplo:
'''
class SkibidiToilet:
  def __init__(self, fezes, nome, toalete):
    self.fezes = fezes #Atributos
    self.nome = nome #Atributo
    self.toalete = toalete #Atributo

  def mostrar_o_skibidi(self): #Esse é o método da classe, ele usa os atributos
    print(f"O nível de fezes do seu Skibidi é {self.fezes}, seu nome é {self.nome} e seu toalete é nível {self.toalete}")

s = SkibidiToilet(15, "CALMA TOSCANETO", 5 )
s.mostrar_o_skibidi()
 