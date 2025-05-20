from statistics import mean, median, mode

entrada = input("Digite uma lista de números separados por vírgula: ")

try:
    numeros = [float(num.strip()) for num in entrada.split(",")]

    media = mean(numeros)
    mediana = median(numeros)
    moda = mode(numeros)  

    print(f"Média: {media}")
    print(f"Mediana: {mediana}")
    print(f"Moda: {moda}")

except ValueError:
    print("Erro: Digite apenas números.")
    
