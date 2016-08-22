import socket

#AF_INET specifies connection type
#SOCK_STREAM allows you to make a TCP connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(s)

server = 'pythonprogramming.net'
port = 80

server_ip = socket.gethostbyname(server)
print(server_ip)

request = "GET / \nHost: "+server+"\n\n"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server, 80))
s.send(request.encode())

result = s.recv(4096)

#print(result)

while(len(result) > 0):
    print(result)
    result = s.recv(1024)
