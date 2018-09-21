import socket
BYTES = 1024
ENCODING = 'UTF-8'
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
   s.connect((socket.gethostname(), 8881))
   s.send(input(msg).encode(ENCODING))
   size = int(s.recv(BYTES).decode(ENCODING))
   if size >= 0:
       with open('RECEIVED', 'wb') as f:
           while size > 0:
               data = s.recv(BYTES)
               f.write(data)
               size -= BYTES
   else:
       print('Arquivo não existe')
