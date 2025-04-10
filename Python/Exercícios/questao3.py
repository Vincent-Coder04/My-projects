def verificar_status(nota):
    if nota >= 7:
        print("Aprovado")
    elif 5 <= nota < 7:
        print("Recuperação")
    else:
        print("Reprovado")

nota = float(input("Digite a nota (0 a 10): ")) 
                    
verificar_status(nota) 