#Importing all modules
from asyncio.windows_events import NULL
from random import randint
import os
import random
import secrets
import string
import asyncio
import json

token = NULL
password = NULL
mailPrefix = NULL
mailSuffix = NULL

#USE SO THAT PROGRAM WON'T LAG / CRASH
if os.name in ['nt']:
  asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


#Reads config file & generates token depending on length given
config = open("config.json")
cData = json.load(config)
for i in cData["TokenLength"]:
  if int(i) == 4:
    token = random.randint(1000, 9999)

  elif int(i) == 5:
    token = random.randint(10000, 99999)

  elif int(i) == 6:
    token = random.randint(100000, 999999) 

  elif int(i) < 4 or int(i) > 6:
    print("[400] Please don't use a token length smaller than 4 or longer than 6 - check config.json")





#Creates logs folder - IF NOT DONE ALREADY (saving all generated tokens, passwords etc.)
if not os.path.exists("logs"):
  os.makedirs("logs")


#Generates 16 char password including symbols
alphabet = string.ascii_letters + string.digits
password = ''.join(secrets.choice(alphabet) for i in range(16))


#Creating log files for each generated token
for i in cData["EnableLogs"]:
  if int(i) == 1:
    mailPrefix = cData["EmailPrefix"]
    mailSuffix = cData["EmailSuffix"]

    save_path = "logs"
    file_name = token
    completeName = os.path.join(save_path, str(file_name))

    log = open(completeName + ".txt", "w")
    log.write(f"Token: " + str(token) + "\n")
    log.write(f"Mail: " + mailPrefix + str(token) + "@" + mailSuffix + "\n")
    log.write(f"PW: " + str(password))
    log.close

  elif int(i) == 0:
    print("[WARNING]: Logfiles are currently disabled, no logs created.")

  elif int(i) != 1 and 0:
    print("Error [401]: Check config.json") 



#Prints out all the needed data to create an account
print(f"Token: " + str(token))
print(f"Mail: " + mailPrefix + str(token) + mailSuffix)
print(f"PW: " + str(password))









