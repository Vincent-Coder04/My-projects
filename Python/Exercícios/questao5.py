def verificar_temperatura(temperatura):
    if temperatura <= 18:
        print("Frio")
    elif 18 <= temperatura < 25:
        print("Agradavel")
    else:
        print("calor")

temperatura = float(input("Digite uma temperatura em celsius: ")) 
                    
verificar_temperatura(temperatura)  