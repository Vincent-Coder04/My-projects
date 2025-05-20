import random
import string


caracteres = string.ascii_letters + string.digits + string.punctuation

senha = ''.join(random.choice(caracteres) for _ in range(10))

print("Senha gerada:", senha)