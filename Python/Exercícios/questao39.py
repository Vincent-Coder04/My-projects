import random
import string

def gerar_palavra_aleatoria(comprimento):
  letras = string.ascii_lowercase  
  palavra = ''.join(random.choice(letras) for _ in range(comprimento))
  return palavra

comprimento_palavra = 10
palavra_aleatoria = gerar_palavra_aleatoria(comprimento_palavra)
print(f"Palavra aleatória: {palavra_aleatoria}")