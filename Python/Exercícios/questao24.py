def calcular_notas():
    total_geral = 0
    aprovados = 0

    for i in range(1, 6): 
        print(f"Aluno {i}")
        soma_notas = 0
        for j in range(1, 4): 
            nota = float(input(f"Digite a nota {j}: "))
            soma_notas += nota
        media = soma_notas / 3
        total_geral += media
        print(f"Média do aluno {i}: {media:.2f}")
        if media >= 7:
            aprovados += 1

    media_geral = total_geral / 5
    print(f"\nMédia geral da turma: {media_geral:.2f}")
    print(f"Quantidade de alunos aprovados: {aprovados}")

calcular_notas()