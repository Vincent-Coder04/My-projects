def tabuada_completa():
     while True:
        numero = int(input("Digite um número para consultar a tabuada"))
        print(f"Segue a tabuada do número{numero}")

        for i in range(1, 11):
            resultado = numero * i 
            print(f"{numero} x {i} = {numero*i}")
        repetir = input ("Deseja ver outra tabuada? (S/N)")
        if repetir.lower() != "s":
            print("Encerrando...")
            break 
  
tabuada_completa()
