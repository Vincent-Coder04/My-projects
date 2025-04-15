def valor_real():
    valor = float(input("Digite um valor em reais (R$):")) 
    if valor == 0:
        print("Zero não é um valor válido")
    else:
     valor_dolar = valor / 5.20
     print(f"Seu valor em dolar é:{valor_dolar:.2f}US$")

valor_real() 

    