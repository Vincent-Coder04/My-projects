import math

def calcular_notas():
 
    alunos = int(input("Digite o número de alunos para colocar as notas: "))
  
    numero_de_notas = []

    for i in range(1, alunos + 1):
        aluno = float(input(f"Digite a nota do {i}° aluno: "))
        numero_de_notas.append(aluno)

    soma_notas = sum(numero_de_notas)

    media = soma_notas / alunos

    notas_acima_media = [nota for nota in numero_de_notas if nota > media]
    
    print(f"\nSoma de todas as notas: {soma_notas:.2f}")
    print(f"Média das notas: {media:.2f}")
    print(f"Notas acima da média: {notas_acima_media}")

calcular_notas()
