def questao19():

 palavra = input("Digite uma palavra: ")

 quantidade_vogais = 0
 quantidade_consoantes = 0

 vogais = "aeiouAEIOU"
 for letra in palavra:
    if letra in vogais:
        quantidade_vogais += 1
    else:
        quantidade_consoantes +=1

 print(f"A palavra '{palavra}' tem {quantidade_vogais} vogais.")
 print(f"A palavra '{palavra}' tem {quantidade_consoantes} consoantes")
questao19()
