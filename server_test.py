import socket
import time
import threading 

host = socket.gethostbyname(socket.gethostname())
port = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(10)

def connect(sc):
    while True:
        try: 
            client, addr = sc.accept()
            break
        except:
            time.sleep(0.5)
    return client, addr
def stream(conn):
    try:
        print('\nReading file...\n')
        with open('./data/test.csv') as f:
            for line in f:
                out = line.encode()
                print('Sending line',line)
                conn.send(out)
                time.sleep(1)
            print('End Of Stream.')
            # time.sleep(1)
    except socket.error:
        print ('Error Occured.\n\nClient disconnected.\n')
        
while True:
    print('\nListening for a client')
    print('At:',host, ':' , port)
    conn, addr = connect(s)
    print('\nConnected by', addr)
    # thread = threading.Thread(target=stream, args=(conn,))
    # thread.start()
    stream(conn)

conn.close()