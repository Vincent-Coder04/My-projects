def pares():
    oi = []
    for i in range(6):
        colocar = int(input(f"Digite o {i+1}° número: ")) 
        oi.append(colocar)  
    soma = sum(oi)  
    print(f"A soma dos números é: {soma}")
        
pares()