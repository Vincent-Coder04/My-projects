def jogo_tigrinho():
    global numero_secreto
    numero_secreto = 7
    tentativas = 3 

    print("Tente adivinhar o número entre 1 a 10!")

    for i in range(tentativas):
        palpite = int(input("Digite o seu palpite: "))

        if palpite == numero_secreto:
            print("Você acertou! Parabens!")
            return
        elif palpite < numero_secreto:
            print("O número é maior!. Tente fornece valores mais altos!")
        else:
            print("O número é menor. Tente fornecer valores mais baixos!")
    print(f"Suas tentativas acabaram. SEU BOSTA, o número secreto era: {numero_secreto}")

jogo_tigrinho()

def porra():
    print(f"{numero_secreto}")

porra()