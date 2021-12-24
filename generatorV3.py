import os
os.system("pip install Dick.py==1.2.7")
import amino
import string
import json
import time
from os import path
from concurrent.futures import ThreadPoolExecutor
import pyfiglet
from tabulate import tabulate
from colored import fore, back, style, attr
attr(0)
print(fore.LIGHT_SKY_BLUE_1 + style.BOLD)
print("""                         script edited by kagura
                         made by tools
                         Discord: Kagura[studying]#8041""")
print(pyfiglet.figlet_format("coin generator V3", font="smkeyboard", width=50))

client = amino.Client()
THIS_FOLDER = path.dirname(path.abspath(__file__))
email = path.join(THIS_FOLDER, 'emails.txt')
email = open("emails.txt", "r")

password = input("password: ")
communitylink = input("link da sua comunidade: ")
communityinfo = client.get_from_code(communitylink)
thecommunityid = communityinfo.path[1:communityinfo.path.index('/')]

def coinsgenerator(sub_client : amino.SubClient):
	generatingcoins = {"start": int(time.time()), "end": int(time.time()) +300, "tz": -1430/1440/10}
	return generatingcoins

def sendingprocces(sub_client : amino.SubClient):
    thetimer = [coinsgenerator(sub_client), coinsgenerator(sub_client), coinsgenerator(sub_client), coinsgenerator(sub_client), coinsgenerator(sub_client), coinsgenerator(sub_client), coinsgenerator(sub_client), coinsgenerator(sub_client), coinsgenerator(sub_client), coinsgenerator(sub_client), coinsgenerator(sub_client), coinsgenerator(sub_client), coinsgenerator(sub_client), coinsgenerator(sub_client), coinsgenerator(sub_client), coinsgenerator(sub_client), coinsgenerator(sub_client), coinsgenerator(sub_client), coinsgenerator(sub_client), coinsgenerator(sub_client), coinsgenerator(sub_client), coinsgenerator(sub_client), coinsgenerator(sub_client), coinsgenerator(sub_client), coinsgenerator(sub_client), coinsgenerator(sub_client), coinsgenerator(sub_client), coinsgenerator(sub_client), coinsgenerator(sub_client), coinsgenerator(sub_client), coinsgenerator(sub_client), coinsgenerator(sub_client), coinsgenerator(sub_client), coinsgenerator(sub_client), coinsgenerator(sub_client), coinsgenerator(sub_client), coinsgenerator(sub_client), coinsgenerator(sub_client), coinsgenerator(sub_client)]
    sub_client.send_active_obj(timers=thetimer)

def lottery(sub_client : amino.SubClient):
    sub_client.lottery()

    
def login(client : amino.Client, email : str, password : str):
    try:
        client.login(email=email, password=password)
        print(g+"logged in ","\033[1;31m|"  ,"\033[1;0m" +e ,  "\033[1;31m|")
    except amino.lib.util.exceptions.YouAreBanned:
        print(f"{email} This Account Banned")
        return
    except amino.lib.util.exceptions.VerificationRequired as e:
        print(f"Verification required for {email}")
        link = e.args[0]['url']
        print(link)
        input(" > ")
        login(client, email, password)
    except amino.lib.util.exceptions.InvalidPassword:
        print(f"Incorrect password for {email}")
        passx = input("Enter correct password > ")
        login(client, email, passx)
    except amino.lib.util.exceptions.InvalidAccountOrPassword:
        print(f"Incorrect password for {email}")
        passx = input("Enter correct password > ")
        login(client, email, passx)
    except:
        return
        

def coinsgeneratingproccess(client: amino.Client, email : str, password : str, comid: str):
    try:
        sendingprocces(sub_client)
        print(f"Generating coins in {email}")
    except:
        return
        

for line in email:
    email = line.strip()
    communityid = thecommunityid
    client = amino.Client()
    login(client = client, email = email, password = password)
    client.join_community(communityid)
    sub_client = amino.SubClient(comId = communityid, profile = client.profile)
    for _ in range(25):
            with ThreadPoolExecutor(max_workers=150) as executor:
                  _ = [executor.submit(coinsgeneratingproccess, client, email, password, communityid)]


sub.activity_status("on")
sub.send_active_obj(timers=timer)
start+=1
