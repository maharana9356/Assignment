# works on window operating system

import Main as data
from threading import*

data.create("Rahul", {"girlfriend":"yes", "Number":10}, 10)
#to create a key with key_name,value given and with time-to-live property value given(number of seconds)

data.create("Golu", {"girlfriend":"No", "Number":0})
#to create a key with key_name,value given and with no time-to-live property

temp = data.read("Rahul")
#it returns the value of the respective key in Jasonobject format if the TIME-TO-LIVE IS NOT EXPIRED and if the key is present in fle else it returns an ERROR
print(temp)

data.delete("Rahul")
#it deletes the respective key and its value from the file if the TIME-TO-LIVE IS NOT EXPIRED and if the key is present in fle else it returns an ERROR

data.create("Golu", {"girlfriend":"No", "Number":0})
#returns error as key already exist


#now  to access data store using multiple thread
#parallel processing of methods create,read,delete
t1=Thread(target=data.create,args=("Vaibhav", {"girlfriend":"yes", "Number":10}, 10))
t2=Thread(target=data.read,args=("Vaibhav",))
t3=Thread(target=data.delete,args=("Vaibhav",))

t1.start()
t2.start()
t3.start()


