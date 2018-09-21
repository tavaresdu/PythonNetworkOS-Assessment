import socket
import os.path
BYTES = 4096
ENCODING = 'UTF-8'
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
   server.bind((socket.gethostname(), 8881))
   server.listen()
   while True:
       (client, address) = server.accept()
       path = client.recv(BYTES).decode(ENCODING)
       if os.path.isfile(path):
           size = os.stat(path).st_size
           client.send(str(size).encode(ENCODING))
           with open(path, 'rb') as f:
               data = f.read(BYTES)
               while data:
                   client.send(data)
                   data = f.read(BYTES)
       else:
           client.send('-1'.encode(ENCODING))
