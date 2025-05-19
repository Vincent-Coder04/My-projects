def calcular_pagamento(horas_trabalhadas, valor_hora):
    total_dia = horas_trabalhadas * valor_hora
    print(f"Total do dia: R${total_dia:.2f}")
    
    if horas_trabalhadas > 8:
     print("Hora extra registrada!")
while True:
 try:
  horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))
  valor_hora = float(input("Digite o valor da hora: "))
  break
 except ValueError:
  print("Digite um valor númerico")
  continue
  
calcular_pagamento(horas_trabalhadas, valor_hora) 
