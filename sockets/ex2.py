import socket

#AF_INET specifies connection type
#SOCK_STREAM allows you to make a TCP connection

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

target = input('What website to scan?: ')

def pscan(port):
    try:
        con = s.connect((target,port))
        return True
    except:
        return False


for x in range(1,25):
    if pscan(x):
        print('Port',x,'is open')
    else:
        print('Port',x,'is closed')
