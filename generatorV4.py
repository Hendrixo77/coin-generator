from os import _exit,system
import time
import json
import sys

from amino.lib.util import exceptions
try:
	import os
	os.system("pip install Dick.py==1.2.7")
	import amino
except:
    print("not have internet")
import string
import threading
import pyfiglet
from tabulate import tabulate
from colored import fore, back, style, attr
attr(0)
print(fore.LIGHT_SKY_BLUE_1 + style.BOLD)
print("""                         script edited by kagura
                         made by kira-xc
                         Discord: Kagura[studying]#8041""")
print(pyfiglet.figlet_format("coin generator V4", font="smkeyboard", width=50))

from datetime import datetime
def num5():
    return {"start":int(datetime.timestamp(datetime.now())),"end":int(datetime.timestamp(datetime.now()))+300}

def timero():  
    return [
num5(),num5(),num5(),num5(),num5(),num5(),num5(),num5(),num5(),num5(),num5(),num5()
,num5(),num5(),num5(),num5(),num5(),num5(),num5(),num5(),num5(),num5(),num5(),num5(),
num5(),num5(),num5(),num5(),num5(),num5(),num5(),num5(),num5(),num5(),num5(),num5()

]
comlist=['133937342']
timer=timero()
def joiner(m):
    try:
        client.join_community(m)
        print("joined in ",m)
    except:
        print("error to join to from : "+m)
cpt=0
def taskos(comId):
    sub=amino.SubClient(comId=comId,profile=client.profile)  
    sub.activity_status("on")
    sub.send_active_obj(timers=timer)
    print("filish to log in the email : "+email)
endos=False
while endos==False:
    with open('email.json') as json_file:
        data = json.load(json_file)
        listos=[]
        passwords=[]
        devices=[]
        for d in range(0,len(data)):
            listos.append(data[d]['email'])
            passwords.append(data[d]['password'])
            devices.append(data[d]['device'])
    
    for email,password,device in zip(listos,passwords,devices):
        client=amino.Client(deviceId=device)
        threads=[] 
        threads2=[]
        try:
            client.login(email=email,password=password)
        except Exception as e:
            print(e)
            _exit(1)
        comIds=client.sub_clients(start=0,size=200).comId
        if len(comIds)<10:
            for comos in comlist:
                threads2.append(threading.Thread(target=joiner, args=(comos,)))
            for t2 in threads2:
                if not t2.is_alive():
                    t2.start()
            for t2 in threads2:
                t2.join()
            comIds=client.sub_clients(start=0,size=200).comId
        for comId in comIds:
            timer=timero()
            cpt=0
            threads.append(threading.Thread(target=taskos, args=(comId,)))
        for t in threads:
            if not t.is_alive():
                t.start()
        for t in threads:
            t.join()
        client.logout()
    endos=False if input("to be continued ? y/n : ")!="n" else True
_exit(1)
