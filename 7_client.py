import socket
import pickle
BYTES = 1024
ADDRESS = (socket.gethostname(), 9991)
GB = 1073741824
print('INICIANDO CLIENTE')
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
   requests = ['TOTAL', 'DISP']
   print('ENVIANDO REQUISIÇÃO PARA O SERVIDOR')
   s.sendto(pickle.dumps(requests), ADDRESS)
   print('RECEBENDO RESPOSTA DO SERVIDOR')
   (response, server) = s.recvfrom(BYTES)
   response = pickle.loads(response)
   print('TOTAL DO DISCO:', response[0] / GB, 'GB')
   print('DISCO DISPONÍVEL:', response[1] / GB, 'GB')