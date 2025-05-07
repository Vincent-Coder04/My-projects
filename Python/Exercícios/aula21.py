class Aluno:
    def __init__(self, nome):
      self.nome = nome 
      self.notas = []

    def adicionar_nota(self, nota):
       self.notas.append(nota)
    
    def calcular_media(self):
       if self.notas:
          return sum(self.notas) / len(self.notas)
       else:
          return 0 

    def exibir_informacoes(self):
       media = self.calcular_media()
       print(f"{self.nome} - Notas: {self.notas} - Média: {media}")

def menu_aluno():
   nome = input("Digite o seu nome: ")
   aluno = Aluno(nome)

   while True:
      print("1 - Adicionar nota")
      print("2 - Ver informações do aluno")
      print("3 - Sair")
      opcao = input("Escolha uma opção: ")
     
      if opcao == "1":
       try:
         nota = float(input("Digite a nota: "))
       except ValueError:
          print("Digite um número por favor")
      elif opcao == "2": 
         aluno.exibir_informacoes()
         return
      elif opcao == "3":
         print("Saindo...")
         break
      else:
         print("Opção Inválida\n")

menu_aluno()        
 