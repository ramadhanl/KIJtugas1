import socket
import threading
import json
import struct


class client:
    

    def __init__(self,address="localhost",port=8990):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.address = "localhost"
        self.port = 8990
        self.username=""
        self.password=""
        self.session_key=""


    def connect(self):
        self.s.connect((self.address,self.port))
    
    def send(self,data):
        send_data = json.dumps(data)
        print("send to server" + str(data)+"\n")
        #send_data = struct.pack('>I',str(len(send_data)) +send_data
        self.s.sendall(send_data.encode())

    def recvall(self,sock,count):
        buff =b''
        while(len(buff)<count):
            newbuff = sock.recv(count)
            if not newbuff : return None
            buff+=newbuff
        return buff

    def receive(self):
        #lengthbuff = self.recvall(self.s,4)
        #length = struct.unpack('>I',lengthbuff)[0]
        #data = self.recvall(self.s,length)
        data = self.s.recv(2048).decode()
        message=json.loads(data)
        print("from server :" +str(message) +"\n")
        if(message['flag']=='DATA'):
            return message


#cl = client()
#cl.connect()

#while 1:
#    message = input("Enter your Message :\n")
#    cl.send_string(message)
#    print(threading.active_count)



