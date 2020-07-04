import socket
import os

HOST=''
PORT=9876
ADDR=(HOST,PORT)
BUFSIZE=4096

serv=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

serv.bind(ADDR)
serv.listen(5)

print("listening")

while True:
    conn,addr = serv.accept()
    print("client connected",addr)

    #recieve string command to see what the client wants
    data = conn.recv(BUFSIZE)

    if data.decode()=="backup":
        myfile=open("backup.zip","wb")
        while True:
            data=conn.recv(BUFSIZE)
            if not data: break
            myfile.write(data)
            print("writing file")
        myfile.close()
        print("finished writing file")
        

    elif data.decode()=="restore":
        #check to see if backup.zip exists
        if os.path.isfile("backup.zip")==True:
           totalBytes = open("backup.zip","rb").read()
           conn.send(totalBytes)
            

    #close connection
    conn.close()
    print("client disconnected")


