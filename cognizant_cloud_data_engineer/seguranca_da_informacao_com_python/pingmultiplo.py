import os
import time

with open('hosts.txt') as file:
    dump = file.read()
    dump = dump.splitlines()

    #Para cada um dos IPs no arquivo, executa ping
    for ip in dump:
        print("Verificando ip ", ip)
        print("-" * 80)
        os.system('ping -n 2 {}'.format(ip))
        print("-" * 80)
        time.sleep(5)