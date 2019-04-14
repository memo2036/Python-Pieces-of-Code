import socket
import zipfile

##A Server will create the output file
##The server work
def ServerSide():
    host = 'Localhost'
    port = 8080
    address = (host, port)
    buf_size=1024
    myServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    myServer.bind(address)
    myServer.listen(1)
    conn, addr = myServer.accept()
    print ("Connection from: " + str(addr))
    
    while True:
            data = conn.recv(1024).decode()
            if not data:
                    break
            data = data.upper()
            Mess = data + 'Echoooooooooooo'
            conn.send(Mess.encode())
    conn.close()
##end of the server

if __name__ == '__main__':
    ServerSide()
