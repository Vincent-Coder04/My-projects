def caixa_eletronico():
      valor = int(input("Digite o valor que será sacado(mútiplo de 10)"))

      if valor % 10 !=0:
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
             
      