#Gerador de senhas
import random
import string

tamanho = int(input("Digite o tamanho da senha a ser gerada: "))

chars = string.ascii_letters + string.digits + 'ç!@#$%&*()-=+_,.;:/?'

rnd = random.SystemRandom()

print(''.join(rnd.choice(chars) for i in range(tamanho)))