#Importing all modules
from asyncio.windows_events import NULL
import os
import random
import secrets
import string
import asyncio
import json

timesGenerated = NULL

#USE SO THAT PROGRAM WON'T LAG / CRASH
if os.name in ['nt']:
  asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


#Creates logs folder - IF NOT DONE ALREADY (saving all generated tokens, passwords etc.)
if not os.path.exists("logs"):
  os.makedirs("logs")


#Gives out a random number used as a token for future mail & XBox Gamertag
token = random.randint(1000, 9999)


#Generates 16 digit password including symbols
alphabet = string.ascii_letters + string.digits
password = ''.join(secrets.choice(alphabet) for i in range(16))


#Creating log files for each generated token
save_path = "logs"
file_name = token
completeName = os.path.join(save_path, str(file_name))

log = open(completeName + ".txt", "w")
log.write(f"Token: " + str(token) + "\n")
log.write(f"Mail: accdatagen" + str(token) + "@gmail.com\n")
log.write(f"PW: " + str(password))
log.close


#Prints out all the needed data to create an account
print(f"Token: " + str(token))
print(f"Mail: accdatagen" + str(token) + "@gmail.com")
print(f"PW: " + str(password))









