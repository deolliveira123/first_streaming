import socket as sck
import time

HOST = "localhost"
PORT = 3000

s = sck.socket()
s.bind((HOST, PORT))

print(f"aguardando conexão na {PORT}")

s.listen(5)

conn, address = s.accept()

print(f"recebendo solicitação de {address}")

messages = [

    'hoje',
    'kevin',
    'Durant',
    'é',
    'o',
    'Melhor',
    'score da liga'
]

for msg in messages:
    msg = bytes(msg, 'utf-8')
    conn.send(msg)
    time.sleep(2)

conn.close()
