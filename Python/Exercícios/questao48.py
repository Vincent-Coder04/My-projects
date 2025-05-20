produtos = {}

for i in range(3):
    nome = input(f"Digite o nome do {i+1}º produto: ")
    preco = float(input(f"Digite o preço de '{nome}': R$ "))
    produtos[nome] = preco

print("\nProdutos cadastrados:")
for nome, preco in produtos.items():
    print(f"{nome}: R$ {preco:.2f}")

media = sum(produtos.values()) / len(produtos)
print(f"\nA média dos preços é: R$ {media:.2f}")