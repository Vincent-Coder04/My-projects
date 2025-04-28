def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero."
    return a / b

while True:
    print("\nMenu:")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Sair")
    
    escolha = input("Escolha uma opção: ")
    
    if escolha == "5":
        print("Saindo...")
        break

    if escolha not in ["1", "2", "3", "4"]:
        print("Opção inválida.")
        continue

    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Entrada inválida. Digite números.")
        continue

    if escolha == "1":
        print(f"Resultado: {somar(num1, num2)}")
    elif escolha == "2":
        print(f"Resultado: {subtrair(num1, num2)}")
    elif escolha == "3":
        print(f"Resultado: {multiplicar(num1, num2)}")
    elif escolha == "4":
        print(f"Resultado: {dividir(num1, num2)}")