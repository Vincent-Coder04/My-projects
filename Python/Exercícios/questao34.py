import time

segundos = int(input("Digite o número de segundos para o cronômetro: "))

for i in range(segundos, -1, -1):
    print(i)
    time.sleep(1)  

print("Tempo encerrado!")
         