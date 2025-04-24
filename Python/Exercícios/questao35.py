import os

while True:
    nome_pasta = input("Digite o nome da nova pasta ou digite 'sair' para encerrar: ").lower()
    if nome_pasta == "sair":
        print("Encerrando...")
        break
    if not os.path.exists(nome_pasta):
        print(f"A pasta '{nome_pasta}' não existe")
        nome_pasta = input("Digite o nome da nova pasta ou digite 'sair' para encerrar: ").lower()
    else:
        print(f"A pasta '{nome_pasta}' já existe.")
    print("Arquivos e diretórios no diretório atual:")
    for item in os.listdir():
        print(item) 