def aplicar_desconto():
    # Pergunta o valor do produto
    preco = float(input("Digite o valor do produto (em R$): "))
    
    # Verifica se o valor é maior que 100 para aplicar o desconto
    if preco > 100:
        desconto = preco * 0.10  # Calcula 10% de desconto
        preco_com_desconto = preco - desconto  # Aplica o desconto
        print(f"Desconto aplicado de R${desconto:.2f}. O valor final é R${preco_com_desconto:.2f}.")
    else:
        print(f"Produto sem desconto. O valor é R${preco:.2f}.")
        
# Chama a função
aplicar_desconto()