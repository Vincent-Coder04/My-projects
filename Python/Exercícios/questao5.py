def verificar_temperatura(temperatura):
    if temperatura <= 18:
        print("Frio")
    elif 18 < temperatura < 25:
        print("Agradável")
    else:
        print("Calor")

while True: 
    entrada = input("Digite a temperatura em Celsius (exemplo: 20°C): ")

    if entrada.endswith("°C") or entrada.endswith("C"):
        try:
            
            temperatura = float(entrada[:-2])  
            verificar_temperatura(temperatura)
            break  
        except ValueError:
            print("Por favor, digite um número válido antes do símbolo de grau.")
    else:
        print("Por favor, inclua o símbolo de grau '°C' ao final da temperatura.")
    