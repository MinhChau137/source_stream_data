import socket
from time import sleep

host = socket.gethostbyname(socket.gethostname())
port = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
while True:
    print('\nListening for a client at',host , port)
    conn, addr = s.accept()
    print('\nConnected by', addr)
    try:
        print('\nReading file...\n')
        with open('./data/test.csv') as f:
            for line in f:
                out = line.encode()
                print('Sending line',line)
                conn.send(out)
                sleep(1)
            print('End Of Stream.')
            sleep(1)
    except socket.error:
        print ('Error Occured.\n\nClient disconnected.\n')
conn.close()