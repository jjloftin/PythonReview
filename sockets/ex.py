import socket

#AF_INET specifies connection type
#SOCK_STREAM allows you to make a TCP connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(s)

server = 'pythonprogramming.net'
port = 80

server_ip = socket.gethostbyname(server)
print(server_ip)

request = "GET \ HTTP/1,1\nHost: "+server+"\n\n"
s.connect((server,port))
s.send(request.encode())

result = s.recv(4096)

print(result)
