import socket
import pickle
BYTES = 4096
ADDRESS = (socket.gethostname(), 30883)
TENTATIVAS = 6
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.settimeout(5)
    requests = ['TOTAL', 'DISP']
    print('Enviando Requisição')
    s.sendto(pickle.dumps(requests), ADDRESS)
    while TENTATIVAS > 0:
        try:
            print('Aguardando resposta')
            (response, server) = s.recvfrom(BYTES)
            response = pickle.loads(response)
            print('Total de Memória:', response[0], 'Bytes')
            print('Memória Disponível:', response[1], 'Bytes')
            TENTATIVAS = 6
            break
        except socket.timeout:
            TENTATIVAS -= 1
            if TENTATIVAS > 0:
                print('Tempo expirado. Tentativas restantes:', TENTATIVAS)
            else:
                print('Tempo expirado. Encerrando programa.')
