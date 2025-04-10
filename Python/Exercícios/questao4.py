def calcular_pagamento(horas_trabalhadas, valor_hora):
    total_dia = horas_trabalhadas * valor_hora
    print(f"Total do dia: R${total_dia}")
    
    if horas_trabalhadas > 8:
        print("Hora extra registrada!")

horas = float(input("Digite a quantidade de horas trabalhadas: "))
valor = float(input("Digite o valor da hora: "))
calcular_pagamento(horas, valor)