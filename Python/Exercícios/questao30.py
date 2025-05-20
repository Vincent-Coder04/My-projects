for i in range(1, 4): 
    palavra = input(f"Digite a {i}ª palavra: ")
    ''
    num_vogais = 0
    num_consoantes = 0
    num_espacos = 0
    caracteres_nao_letras = []  
    
    for letra in palavra.lower():
        if letra in "aeiou":
            num_vogais += 1
        elif letra == " ":
            num_espacos += 1
        elif letra.isalpha():
            num_consoantes += 1
        else:
            
            caracteres_nao_letras.append(letra)

  
    print(f"--- Resultado para a palavra {i} ---")
    print(f"Palavra: {palavra}")
    print(f"Número de vogais: {num_vogais}")
    print(f"Número de consoantes: {num_consoantes}")
    print(f"Número de espaços: {num_espacos}")
    
    
    if caracteres_nao_letras:
        print(f"Caracteres que não são letras: {', '.join(caracteres_nao_letras)}")
    else:
        print("Não há caracteres que não sejam letras.")
    

        