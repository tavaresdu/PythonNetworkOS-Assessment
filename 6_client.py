import socket
import pickle
BYTES = 4096
path = input('Escreva o diretório: ')
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((socket.gethostname(), 29716))
    s.send(pickle.dumps(path))
    files = pickle.loads(s.recv(BYTES))
    if files != 0:
        for f in files:
            print(f)
    else:
        print('Diretório não encontrado!')
