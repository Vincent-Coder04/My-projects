def calcular_media():
 nota1 = float(input("Digite a primeira nota: "))
 nota2 = float (input("Digita a segunda nota: "))
 nota3 = float (input("Digita a terceira nota: "))
 media = (nota1 + nota2 + nota3) / 3

 if media >= 7:
  print("Aprovado")
  print(f"A média é: {media:.2f}")
 elif 5 <= media < 7:
  print("Recuperação")
  print(f"A média é: {media:.2f}")
 else:
  print("Reprovado")
  print(f"A média é: {media:.2f}")
calcular_media()
