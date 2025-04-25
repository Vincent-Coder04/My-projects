def relogio_digital():
    horas_limite = int(input("Digite o número de horas para simular: "))

    for hora in range(horas_limite):
        for minuto in range(60):
            for segundo in range(60):
                print(f"{hora:02d}:{minuto:02d}:{segundo:02d}")
                
relogio_digital()  
    