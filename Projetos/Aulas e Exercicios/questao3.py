def verificar_status(nota):
    # Verifica a faixa de notas e exibe o status correspondente
    if nota >= 7:
        print("Aprovado")
    elif 5 <= nota < 7:
        print("Recuperação")
    else:
        print("Reprovado")

# Recebe a nota do usuário e chama a função
nota = float(input("Digite a nota (0 a 10): "))  # Recebe a nota do usuário
verificar_status(nota)  # Chama a função para verificar o status