from collections import Counter

frase = input("Digite uma frase qualquer: ")
contagem = Counter(frase)

caracteres_repetidos = {char for char, qtd in contagem.items() if qtd > 1}

print("Caracteres que se repetem:", caracteres_repetidos)