def media_notas():
    notas = [5.9, 8.5, 9.9, 9.7]
    media = sum(notas) / len(notas)
    print(f"As notas existentes são: {notas}")
    print(f"A média final é: {media:.2f}")

media_notas()
