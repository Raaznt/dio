import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("A conexao falhou")
        print("Error: {}".format(e))
        sys.exit()
    else:
        print("Socket criado com sucesso")

    HostAlvo = input("Digite o host ou IP a ser conectado: ")
    PortaAlvo = input("Digite a porta a ser conectada: ")

    try:
        s.connect((HostAlvo, int(PortaAlvo)))
        print("CLiente TCP conectado com sucesso no host {host}"
              " na porta {port}".format(host=HostAlvo, port = PortaAlvo))
    except socket.error as e:
        print("A conexao falhou.\n"
              "Nao foi possivel conectar no host {host} na porta {port}"
              .format(host = HostAlvo, port = PortaAlvo))
        sys.exit()

    finally:
        s.shutdown(2)

if __name__ == "__main__":
    main()
