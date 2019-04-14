import socket

##def ClientSide():
host = 'localhost'
port = 8080
address = (host, port)
 
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.connect(address)
 
message = input("Enter your message or q to quit -> ")
 
while message != 'q':
        mySocket.send(message.encode())
        data = mySocket.recv(1024).decode()
        print ('Received from server: ' + data)
        message = input("Enter your Message or q to quit -> ")
         
mySocket.close()
## 
##if __name__ == '__main__':
##    ClientSide
