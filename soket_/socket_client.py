import socket
flag = True
client = socket.socket()

client.connect(('localhost',8080))

while flag:
    msg = input("Enter your message('quit' for quit) :  ").strip()

    if len(msg) == 0:
        print("message can not be empty")
        continue

    client.send(msg.encode())
    if msg != "quit":
        data = client.recv(1024)
        print(str(data,encoding='utf8'))
    else:
        flag = False
client.close()
print("server closed")











