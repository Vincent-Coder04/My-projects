def calcular_total_abastecimento():
    preco_gasolina = 5.59
    preco_alcool = 4.39
    preco_diesel = 5.99

    print("Digite o tipo de combustível:")
    print("1 - Gasolina")
    print("2 - Álcool")
    print("3 - Diesel")
    tipo_combustivel = int(input("Escolha o número correspondente ao combustível: "))
    
    litros = float(input("Digite a quantidade de litros abastecidos: "))
    
    if tipo_combustivel == 1:
        total = litros * preco_gasolina
        print(f"Total a pagar: R$ {total:.2f} (Gasolina)")
    elif tipo_combustivel == 2:
        total = litros * preco_alcool
        print(f"Total a pagar: R$ {total:.2f} (Álcool)")
    elif tipo_combustivel == 3:
        total = litros * preco_diesel
        print(f"Total a pagar: R$ {total:.2f} (Diesel)")
    else:
        print("Opção inválida. Por favor, escolha um número entre 1 a 3.")

calcular_total_abastecimento()