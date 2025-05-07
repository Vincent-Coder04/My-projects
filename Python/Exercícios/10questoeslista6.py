'''
1. (Conceitual)
O que é uma classe em Python?
A) Um tipo especial de lista = X
B) Um bloco de código com variáveis globais = X
C) Um molde para criar objetos com características e comportamentos = ✅ 
D) Um tipo de função com múltiplos parâmetros = X
'''
'''
2. (Conceitual)
O que são objetos em Programação Orientada a Objetos?
A) Variáveis com nomes maiores = X
B) Instâncias criadas a partir de uma classe = ✅ 
C) Funções que não recebem parâmetros = X
D) Qualquer estrutura de repetição = X
'''
'''
3. (Prática)
Dada a classe abaixo: 
class Pessoa:
def __init__(self, nome):
self.nome = nome
Qual das opções cria corretamente um objeto dessa classe?
A) Pessoa = (&quot;João&quot;) = X
B) pessoa = Pessoa.nome(&quot;João&quot;) = X
C) pessoa = Pessoa(&quot;João&quot;) = ✅ 
D) pessoa = Pessoa[&quot;João&quot;] = X
'''
'''
4. (Prática)
Em uma classe, o que representa o self?
A) A classe como um todo = X
B) Um valor fixo definido no construtor = ✅ 
C) A própria instância (objeto) sendo criada ou manipulada = X
D) Um comando para sair do método = X
'''
'''
5. (Código - Preenchimento)
Complete o código abaixo para que ele funcione corretamente:
class Carro:
def __init__(self, modelo):
self.modelo = modelo
meu_carro = ____________
print(meu_carro.modelo)
'''
class Carro:
    def __init__(self, modelo):
        self.modelo = modelo

meu_carro = Carro("Fusca")
print(meu_carro.modelo)
'''
6. (Conceitual)
Assinale a alternativa que melhor representa a diferença entre classe e objeto:
A) Objeto é a teoria, classe é a prática = X
B) Classe é a definição, objeto é a instância dessa definição = ✅ 
C) Ambos são exatamente a mesma coisa = X
D) Classe serve só para criar funções e não tem atributos = X
'''
'''
7. (Código - Compreensão)
O que será impresso ao executar o seguinte código?
class Animal:
def __init__(self, nome):
self.nome = nome
a = Animal(&quot;Cachorro&quot;)
print(a.nome)
R:Cachorro
'''
class Animal:
 def __init__(self, nome):
  self.nome = nome
a = Animal("Cachorro")
print(a.nome)
'''
8. (Prática)
Qual é a palavra-chave utilizada para definir uma classe em Python?
A) new = X
B) function = X
C) class = ✅ 
D) define = X
'''
'''
9. (Reflexão/Criação)
Explique com suas palavras o que significa instanciar uma classe.
Dê um exemplo prático com o nome de uma classe fictícia.
R:Instanciar uma classe é pegar valores e interligar eles com o comportamento de uma classe estabelecida, como se fosse um exemplo pratico utilizando coisas definidas em uma classe
Exemplo:
'''
class Continentes:
   def __init__(self, africa, america):
      self.africa = africa
      self.america = america
   def apresentar(self):
       print(f"A {self.africa} faz parte da áfrica e o {self.america} faz parte da america")
   def apresentou(self):
       print(f"O {self.africa} faz parte da áfrica e o {self.america} faz parte da america")
p1 = Continentes("Libéria", "Belize")
p2 = Continentes("Malawi", "Suriname")
p1.apresentar()
p2.apresentou()
'''
10. (Análise de código com erro proposital)
Veja o código abaixo. Qual é o erro presente nele?
class Aluno:
def __init__(nome, idade):
nome = nome
idade = idade
A) Está tudo certo = X
B) A classe deveria chamar ClasseAluno = X
C) Faltou o self nos parâmetros e nos atributos = ✅ 
D) O nome idade deveria ser string = X
'''