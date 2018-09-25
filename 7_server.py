import socket
import psutil
import pickle
BYTES = 4096
print('Iniciando Servidor...')
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((socket.gethostname(), 30883))
    while True:
        print('Aguardando requisição...')
        (requests, client) = s.recvfrom(BYTES)
        requests = pickle.loads(requests)
        print('Requisição:', requests)
        response = list()
        memory = psutil.virtual_memory()
        for request in requests:
            if request == 'TOTAL':
                print('Lendo tamanho total de memória...')
                response.append(memory.total)
            elif request == 'DISP':
                print('Lendo tamanho disponível de memória...')
                response.append(memory.available)
        print('Enviando resposta ao cliente...')
        s.sendto(pickle.dumps(response), client)
