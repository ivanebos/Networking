#Networking

import socket

def find_port(host):
    run = True
    while run:
        try:
            port = input()
            s.connect((host,int(port)))
            run = False
        except:
            print("Error connecting to port "+ port)


def main():
    host = '127.0.0.1'
    s = socket.socket()

    find_port(host)
    while message != "q":
        data = s.recv(1024).decode('utf-8')
        print("Recived from sever: " + data)
    s.close()

if __name__ == "__main__":
    main()

