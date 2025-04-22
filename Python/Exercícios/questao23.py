def verificar_primos():
    while True:
        numero = int(input("Digite um número (0 para sair): "))
        if numero == 0:
            print("Encerrando o programa.")
            break

        if numero < 2:
            print(f"{numero} não é primo.")
        else:
            eh_primo = True
            for i in range(2, int(numero**0.5) + 1):
                if numero % i == 0:
                    eh_primo = False
                    break
            if eh_primo:
                print(f"{numero} é primo.")
            else:
                print(f"{numero} não é primo.")
    
verificar_primos()