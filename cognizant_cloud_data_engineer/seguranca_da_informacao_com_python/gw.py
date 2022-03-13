#Gerador de wordlists
import itertools

string = input('String a ser permutada: ')

for j in range(1, (len(string) + 1)):
    resultado = itertools.permutations(string, j)
    for i in resultado:
        print(''.join(i))