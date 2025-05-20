import random 

def dadinho():
    dado = str(input("Escreva qualquer coisa para lançar um dado de 6 lados: "))
    dado = random.randint(1, 6)
    print("O número do seu dado é: ", dado)
    quer = str(input("Quer Jogar Denovo?, Escreva 'Não' para sair, Digite qualquer coisa para continuar: "))
    while True:
     if quer == "Não":
      print("Encerrando...")
      break
     else:
           dado = random.randint(1, 6)
           print("O número do seu dado é: ", dado)
           quer = str(input("Quer Jogar Denovo?, Escreva 'Não' para sair, Digite qualquer coisa para continuar: "))
dadinho()