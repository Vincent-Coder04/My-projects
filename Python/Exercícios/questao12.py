def avaliacao():
    nota1 = float(input("Digite a Primeira nota:"))
    nota2 = float(input("Digite a Segunda nota:"))
    nota3 = float(input("Digite a Terceira nota:"))
    nota4 = float(input("Digite a Quarta nota:"))
    nota5 = float(input("Digite a Quinta nota:"))
    media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5 
    if media >=7:
      print("Aprovado")
    elif 5<= media < 7:
      print("Recuperação")
    else : 
      print("Reprovado")

avaliacao() 