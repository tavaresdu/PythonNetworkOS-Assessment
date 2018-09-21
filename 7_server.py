import socket
import psutil
import pickle
BYTES = 1024
print('Iniciando Servidor...')
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((socket.gethostname(), 27706))
    while True:
        print('Aguardando requisição...')
        (requests, client) = s.recvfrom(1024)
        print('REQUISIÇÃO RECEBIDA')
        requests = pickle.loads(requests)
        response = list()
        partition = psutil.disk_partitions()[0]
        disk = psutil.disk_usage(partition.mountpoint)
        for request in requests:
            if request == 'TOTAL':
                print('LENDO TAMANHO TOTAL DO DISCO')
                response.append(disk.total)
            elif request == 'DISP':
                print('LENDO TAMANHO DISPONÍVEL DO DISCO')
                response.append(disk.free)
        print('ENVIANDO RESPOSTA AO CLIENTE')
        s.sendto(pickle.dumps(response), client)
