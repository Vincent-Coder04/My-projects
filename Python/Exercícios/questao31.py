import math

def operacoes():
    try:
        numero = float(input("Digite um número: "))

        if numero < 0:
            print("Não é possível calcular a raiz quadrada ou logaritmo de número negativo.")
        else:
            raiz = math.sqrt(numero)
            logaritmo = math.log(numero)
            print("A raiz quadrada do número é:", raiz)
            print("O logaritmo do número é:", logaritmo)
            potencia = math.pow(numero, 2)
            seno = math.sin(numero)
            print("A potência do número é:", potencia)
            print("O seno do número é:", seno)
    except:
        print("Você deve digitar um número válido.")

operacoes()
