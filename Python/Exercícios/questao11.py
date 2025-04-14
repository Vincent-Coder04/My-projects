def contar_votos():
    votos_ana = 0
    votos_bruno = 0
    votos_carla = 0
    
    for i in range(5):
        voto = int(input(f"Voto {i + 1}: Escolha um candidato (1 - Ana, 2 - Bruno, 3 - Carla): "))
        
        if voto == 1:
            votos_ana += 1
        elif voto == 2:
            votos_bruno += 1
        elif voto == 3:
            votos_carla += 1
        else:
            print("Voto inválido! Tente novamente.")
            
    print("Resultado final dos votos:")
    print(f"Ana recebeu {votos_ana} votos.")
    print(f"Bruno recebeu {votos_bruno} votos.")
    print(f"Carla recebeu {votos_carla} votos.")

contar_votos()