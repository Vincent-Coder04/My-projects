def pares():
    oi = []
    i = 0
    while i < 6:
        while True:
            try:
                colocar = int(input(f"Digite o {i+1}° número: ")) 
                oi.append(colocar)
                i += 1
                break  
            except ValueError:
                print("Valor inválido! Por favor, digite um número inteiro.")
    
    soma = sum(num for num in oi if num % 2 == 0)
    print(f"A soma dos números pares é: {soma}")

pares()

