def verificar_multiplo():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    if num1 == 0:
        print("Zero não é valido")
    elif num2 == 0:
        print("Zero não é valido")
    elif num1 % num2 == 0:
        print(f"{num1} é múltiplo de {num2}.")
    else:
        print(f"{num1} não é múltiplo de {num2}.")
              
verificar_multiplo()
