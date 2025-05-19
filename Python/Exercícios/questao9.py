'''
def sacar(valor):
    cedulas = [100, 50, 20, 10]
    resultado = {}

    if valor % 10 != 0:
        print("Não é possível sacar esse valor com as cédulas disponíveis.")
        return

    for cedula in cedulas:
        quantidade = valor // cedula
        if quantidade:
            resultado[cedula] = quantidade
        valor %= cedula

    print("Cédulas entregues:")
    for cedula, quantidade in resultado.items():
        print(f"R${cedula}: {quantidade}")

valor = int(input("Digite o valor para saque (múltiplo de 10): "))
sacar(valor) 
'''

def caixa_eletronico():
      try:
       valor = int(input("Digite o valor que será sacado(mútiplo de 10): "))
      except ValueError:
          print("Digite um valor válido")
          
      if valor % 10 != 0:
         print("Valor inválido. O valor deve ser mútiplo de 10")
         return
      else:
         ced100 = valor // 100
         valor %= 100
         ced50 = valor // 50
         valor %= 50 
         ced20 = valor // 20
         valor %= 20
         ced10 = valor //10
         valor %= 10

         print("Notas entregues: ")
         if ced100 > 0:
             print(f"{ced100} notas(s) de R$100.")
         if ced50 > 0:
             print(f"{ced50} notas(s) de R$50.")
         if ced20 > 0:
             print(f"{ced20} notas(s) de R$20.")
         if ced10 > 0:
             print(f"{ced10} notas(s) de R$10.")
             
caixa_eletronico()
             
      