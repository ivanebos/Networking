'''
Port scanner
Ivan ebos
'''
 #!/urs/bin/python

import socket

ip = input("enter the IP address: " )
#port = input("enter the port: ")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

for i in range(0,65535):
    if not sock.connect_ex((ip,i)):
        print("Port ",i," is open")
        
