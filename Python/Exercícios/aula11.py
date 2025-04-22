from datetime import datetime
def mostrar_data_hora():
    agora = datetime.now()
    print("A data e hora de agora é: ")
    print(agora.strftime)
    print(agora.strftime("%d/%m/%Y %H:%M:%S")) 

mostrar_data_hora()

