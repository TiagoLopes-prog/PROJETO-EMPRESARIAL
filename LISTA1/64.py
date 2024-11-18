import random
import string

def gera_senha(tamanho):
    return ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(tamanho))
