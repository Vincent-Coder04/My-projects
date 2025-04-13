def sacar(valor):
    cedulas = [100, 50, 20, 10]
    resultado = {}

    if valor % 10 != 0:
        print("Não é possível sacar esse valor com as cédulas disponíveis.")
        return

    for cedula in cedulas:
        quantidade = valor // cedula
        if quantidade:
            resultado[cedula] = quantidade
        valor %= cedula

    print("Cédulas entregues:")
    for cedula, quantidade in resultado.items():
        print(f"R${cedula}: {quantidade}")

valor = int(input("Digite o valor para saque (múltiplo de 10): "))
sacar(valor) 
