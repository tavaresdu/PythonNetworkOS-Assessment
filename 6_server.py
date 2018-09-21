import socket
import os.path
import pickle
BYTES = 4096
path = '.'
print('Iniciando Server...')
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((socket.gethostname(), 29716))
    server.listen()
    while True:
        print('Aguardando conexão...')
        (client, address) = server.accept()
        path = pickle.loads(client.recv(BYTES))
        print('Diretório recebido:', path)
        if os.path.exists(path):
            files = list()
            for dir in os.scandir(path):
                if dir.is_file():
                    files.append(dir.name)
            client.send(pickle.dumps(files))
            print('Nomes de arquivos enviados!')
        else:
            print('Diretório inexistente!')
            client.send(pickle.dumps(0))
