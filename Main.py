#works on window operating system
import os.path
import os
from os import path
import ast
import time
import json
import sys
from sys import getsizeof
import threading 
from threading import*
##File creation 
filePath = input("Enter file path: ")

#if user enetrs invalid file path error will be returned corresponding to it
#else if user don't enter any path i have assigned a default file path
if len(filePath) != 0:
    if not path.exists(filePath):
        print("error:invalid file path enter correct file path!!!")
        sys.exit()
else:
    filePath = 'D:\\Rah\\Demo'

#print(filePath)
nameOfFile = "Db" 

#then i have given a default file name Db
#and check if on absolute path Db.txt file is not present the we create that file
completeName = os.path.join(filePath, nameOfFile+".txt")         
completePath = os.path.abspath(completeName)
#print(completePath)

if (not path.exists(completePath)):
    file = open(completePath, "w")
    file.write("{}")
    file.close()
    print("File created successfully!!!")

##entry creation in file
f = open(completePath, "r")
fDict = str(f.read())
Dict = json.loads(fDict)
#print(Dict)
fileSize = os.stat(completePath).st_size

def create(key,value,timeout=0):
    if fileSize > 1024*1024*1024:
        print('error: File size exceeded 1GB!!!')
        return

    if key in Dict:
        print("error: this key already exists!!!") #error message1
    else:
        if(key.isalpha()):
            x = json.dumps(value)
            if getsizeof(x) <=(16*1024): #constraints for Jasonobject value less than 16KB
                if timeout==0:
                    EntryVal=[value,timeout]
                else:
                    EntryVal=[value,time.time()+timeout]

                if len(key)<=32: #constraints for input key_name capped at 32chars
                    print("sucsessfully added!!!")
                    Dict[key]=EntryVal
                else:
                    print("error: Key length exceeded 32 chars!!!")
            else:
                print("error: Value memory limit exceeded!! ")#error message2
        else:
            print("error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers!!!")#error message3

    f = open(completePath, "w")
    fDict = json.dumps(Dict) 
    f.write(fDict)
    f.close()

def read(key):
    if key not in Dict:
        print("error: given key does not exist in database. Please enter a valid key!!!") #error message4
    else:
        data=Dict[key]
        if data[1] != 0:
            if time.time()<data[1]: #comparing the present time with expiry time
                value=str(key)+":"+str(data[0]) #to return the value in the format of JasonObject i.e.,"key_name:value"
                return value
            else:
                print("error: time-to-live of ",key," has expired!!!") #error message5
        else:
            value=str(key)+":"+str(data[0])
            return value

def delete(key):
    if key not in Dict:
        print("error: given key does not exist in database. Please enter a valid key!!!") #error message4
    else:
        data = Dict[key]
        if data[1]!=0:
            if time.time() < data[1]: #comparing the current time with expiry time
                del Dict[key]
                print("key is successfully deleted!!!")
            else:
                print("error: time-to-live of ",key," has expired!!!") #error message5
        else:
            del Dict[key]
            print("key is successfully deleted!!!")
    f = open(completePath, "w")
    fDict = json.dumps(Dict) 
    f.write(fDict)
    f.close()

