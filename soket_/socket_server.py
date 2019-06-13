import socket
HOST = '127.0.0.1'
PORT = 8080

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server: #use ipv4 tcp protocol
    server.bind((HOST,PORT))
    server.listen()
    print("redy for work!")

    conn,addr = server.accept()
    print("connection success!")

    flag = True
    while flag:
        data = conn.recv(1024).decode()
        if data != 'quit':
            
            print("accept success : ",data)
            msg=input("enter response ")
            conn.send(msg.encode())
        else:
            flag = False
















