import socket
import pickle
BYTES = 4096
ADDRESS = (socket.gethostname(), 30883)
TENTATIVAS = 6
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    requests = ['TOTAL', 'DISP']
    print('Enviando Requisição')
    s.sendto(pickle.dumps(requests), ADDRESS)
    print('Aguardando resposta')
    (response, server) = s.recvfrom(BYTES)
    response = pickle.loads(response)
    print('Total de Memória:', response[0], 'Bytes')
    print('Memória Disponível:', response[1], 'Bytes')
