from datetime import datetime

agora = datetime.now()
data_formatada = agora.strftime("Hoje é dia %d/%m/%Y e agora são %H:%M.")
print(data_formatada)

resposta = input("Você deseja agendar um compromisso? (s/n): ").lower()

if resposta == 's':
    titulo = input("Digite o título do compromisso: ")
    data_compromisso = input("Digite a data do compromisso (formato DD/MM/AAAA): ")
    compromisso = (f"{titulo} - {data_compromisso}")
    print(f"Compromisso agendado: {compromisso}")
else:
    print("Nenhum compromisso agendado.")

