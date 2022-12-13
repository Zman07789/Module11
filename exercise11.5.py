#By Zackary Paulson
import socket

url = input("Enter a URL: ")

url_components = url.split('/')

host = url_components[2]

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    mysock.connect((host, 80))

    cmd = 'GET '+url+' HTTP/1.0\r\n\r\n'
    cmd = cmd.encode()

    mysock.send(cmd)
except:
    print("Error: URL is improperly formatted or non-existent")
    exit()

while True:
    data = mysock.recv(512)
    if (len(data) < 1) or (data.decode().endswith('\r\n\r\n')):
        break

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode(),end='')

mysock.close()