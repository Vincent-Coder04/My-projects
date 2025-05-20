def aplicar_desconto():
   
    preco = float(input("Digite o valor do produto (em R$): "))
    
    if preco > 100:
        desconto = preco * 0.10  
        preco_com_desconto = preco - desconto  
        print(f"Desconto aplicado de R${desconto:.2f}. O valor final é R${preco_com_desconto:.2f}.")
    else:
        print(f"Produto sem desconto. O valor é R${preco}.")

aplicar_desconto()