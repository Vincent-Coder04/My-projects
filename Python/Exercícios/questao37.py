from datetime import datetime

data_str = input("Digite uma data (ex: 20/10/2025): ")

try:
    data = datetime.strptime(data_str, "%d/%m/%Y")
    dias_semana = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado", "domingo"]
    dia_semana = dias_semana[data.weekday()]
    if dia_semana in ("domingo", "sábado"):
        print(f"A data {data_str} cai em um {dia_semana}.")
    else:
        print(f"A data {data_str} cai em uma {dia_semana}.")
    
except ValueError:
    print("Formato de data inválido. Use o formato DD/MM/AAAA.")
    