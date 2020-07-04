import json
import os
import shutil
import socket
import time
class file_management:

    def __init__(self):
        self.path = os.getcwd() + "/phonebooks/"

    #save dictionary to hdd
    def saveToFile(self,fileName,dictionary):
        jfile = self.path + fileName + '.json'
        json.dump(dictionary,open(jfile,'w'))

    #save dictionary from hdd
    def loadFromFile(self,fileName):
        jfile = self.path + fileName + '.json'
        dictionary = {}
        dictionary = json.load(open(jfile))
        return dictionary

   #delete dictionary from hdd
    def deleteFile(self,fileName):
        jfile = self.path + fileName + '.json'
        os.remove(jfile)

    #view all dictionaries on hdd
    def viewFiles(self):
        print(os.listdir(self.path))


    #zip up all dictionaries and send to server for backup
    def backup_files(self):
        shutil.make_archive("backup","zip",self.path)
        
        ADDR = ("127.0.0.1",9876)
        BUFLIMIT =4096
        zipfile="backup.zip"

        totalBytes = open(zipfile,"rb").read()
        client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client.connect(ADDR)
        client.sendall(b'backup')
        time.sleep(1)
        client.send(totalBytes)
        client.close()
        os.chdir(self.path)
        os.remove("backup.zip")

    #retrieve zip file of backup and unzip and restore original dictionaries from backup save
    def restore_files(self):
        ADDR = ("127.0.0.1",9876)
        BUFLIMIT=4096
        client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client.connect(ADDR)
        client.sendall(b'restore')
        time.sleep(1)
        location=self.path + "backup.zip"
        myfile=open(location,"wb")
        while True:
            data=client.recv(BUFLIMIT)
            if not data: break
            myfile.write(data)
        myfile.close()
        os.chdir(self.path)
        shutil.unpack_archive("backup.zip")
        os.remove("backup.zip")
             




    
