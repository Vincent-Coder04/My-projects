def verificar_status(nota):
    if 7 <= nota < 10:
        print("Aprovado")
    elif 5 <= nota < 7:
        print("Recuperação")
    else:
        print("Reprovado")

while True:
    try:
        
        nota = float(input("Digite a nota (0 a 10): "))

        if 0 <= nota <= 10:
            verificar_status(nota)  
            break  
        else:
            print("Nota inválida! Digite uma nota entre 0 e 10.")
    except ValueError:
        print("Por favor, digite um número válido.")