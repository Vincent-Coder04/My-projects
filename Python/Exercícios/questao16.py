valores = []
for i in range(4):
    valor = float(input(f"Digite o valor da compra {i + 1}: R$ "))
    valores.append(valor)

total = sum(valores)

if total > 200:
    desconto = 0.10
elif total > 100:
    desconto = 0.05
else:
    desconto = 0.0

valor_desconto = total * desconto
total_com_desconto = total - valor_desconto
print("\nResumo da compra:")
print(f"Total sem desconto: R$ {total:.2f}")
print(f"Desconto aplicado: {desconto * 100:.0f}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Total com desconto: R$ {total_com_desconto:.2f}")