## 一、socket 通信协议
1. ![socket通信协议](./picture/socket.png)
2. http、dns、ftp 都是基于 socket 通信的
3. socket api:
   - socket()
   - bind()
   - listen()
   - accept()
   - recv()
   - send()
   - close()
```
# socket 客户端
import socket

# socket.AF_INET 参数表示使用 IPV4，socket.SOCK_STREAM 参数表示使用 TCP 协议连接
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# debug
print(f"s1 : {s}")

s.connect(('www.httpbin.org', 80))

# debug
print(f"s2 : {s}")

s.send(b'GET / HTTP/1.1\r\nHOST:time.geekbang.org\r\nConnection: close\n\r\n')

buffer = []

while True:
    data = s.recv(1024)
    if data:
        buffer.append(data)
    else:
        break
s.close()

response = b''.join(buffer)

header, html = response.split(b'\r\n\r\n', 1)

print(header.decode('utf-8'))

with open('index.html', 'wb') as f:
    f.write(html)
```