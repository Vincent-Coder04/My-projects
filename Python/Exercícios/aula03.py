def calculadora():
    print("Bem'vindo a nossa calculaora!")
    print("Operações válidas: soma, subtracao, multiplicacao, divisao")
    operacao = input("Digite por extenso a operação:").lower()
    numero1 = float(input("Digite o primeiro número"))
    numero2 = float(input("Digite o segundo número"))

    if operacao == "soma":
        resultado = numero1 + numero2
        print(f"O resultado é{resultado}")
    elif operacao == "subtracao":
        resultado = numero1 - numero2
        print (f"O resultado é:{resultado}")
    elif operacao == "multiplicacao":
        resultado = numero1 * numero2
        print(f"O resultado é:{resultado}")
    elif operacao == "divisao":
        if numero2 != 0:
            resultado = numero1 / numero2
            print(f"O resultado é :{resultado}")
        else:
            print("Divisão por 0 não pode acontecer!")
    else:
        print("Operacão inválida")

