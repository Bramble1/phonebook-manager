import json

#wrapper for dictionary, being able to add key values, remove,retrieve,list etc.
class dict_wrapper:

    def __init__(self):
        self.D = {}

    def setEntry(self,key,value):
        self.D[key]=value


    def getEntry(self,key):
        print("[",key,"]=",self.D[key])


    def listEntries(self):
        for key,value in self.D.items():
            print(key,":",value)

    
    def getDictionary(self):
        return self.D


    def setDictionary(self,dictionary):
        self.D = dictionary


    def deleteEntry(self,key):
        del self.D[key]


    def deleteAllEntries(self):
        self.D.clear()


    def deleteDictionary(self):
        del self.D

     


