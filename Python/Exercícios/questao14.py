def questao():
    positivo = 0
    negativo = 0
    zero = 0

    for i in range(6):
        print("Digite um número")
        numero = float(input(f"Número {i + 1}: "))
        
        if numero == 0:
            zero += 1
        elif numero < 0:
            negativo += 1
        else:
            positivo += 1

    print("Contagem de números Positivos, Negativos e Nulos:")
    print(f"{positivo} números positivos.")
    print(f"{negativo} números negativos.")
    print(f"{zero} números nulos.")

questao()