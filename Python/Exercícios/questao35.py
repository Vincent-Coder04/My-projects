import os

downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")

while True:
    nome_pasta = input("Digite o nome da pasta dentro de Downloads (ou 'sair' para encerrar): ").strip()
    
    if nome_pasta.lower() == "sair":
        print("Encerrando...")
        break

    caminho_completo = os.path.join(downloads_path, nome_pasta)

    if not os.path.isdir(caminho_completo):
        print(f"A pasta '{nome_pasta}' não existe dentro da sua pasta Downloads.")
    else:
        print(f"✅ A pasta '{nome_pasta}' existe dentro de Downloads.")
        print("📂 Conteúdo da pasta:")
        for item in os.listdir(caminho_completo):
            print(f"  - {item}")
        