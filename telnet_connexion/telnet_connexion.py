#!/usr/bin/python
from datetime import datetime
import asyncio, telnetlib3
import getpass
import time

port = 23
# server_ip = "10.124.206.68"
# user = "CHATBO"
# password = "1234567890"
# msisdn = ":MSISDN=237669595858:;"
# ZMMI = "ZMMI"+msisdn
# ZMMO = "ZMMO"+msisdn
# ZMMS = "ZMMS"+msisdn
# command = "ZMMO:MSISDN=237669595858:;"
# command = "ZMMO:MSISDN=237663064317:;"

server_ip = input('Enter ip : ')
user = input('Enter username : ')
password = getpass.getpass('Enter password : ')
command = input('Enter command : ')

@asyncio.coroutine
def shell(reader, writer):
    # inc = 1
    # while inc <= 4:
    while True:
        # read stream until '?' mark is found
        outp = yield from reader.read(65536)
        if not outp:
            # End of File
            break
        elif 'ENTER USERNAME' in outp:# and inc == 1:
            writer.write(user)
            writer.write('\n\r' + password + '\n\r' + command + '\n\r')
            # writer.write('\n\r' + password + '\n\r' + ZMMI + '\n\r' + ZMMO + '\n\r' + ZMMS + '\n\r')
            # print(inc)
        # inc += 1
        print(outp)
        # print(len(outp))
        f1 = open("tableau2.txt", "w") #server_ip + "_" + str(datetime.now()) +
        f1.write(outp)
        f1.close()
        time.sleep(2)

    # print(outp)
    # f1 = open("test1.txt", "w") #server_ip + "_" + str(datetime.now()) +

    # f1.write(outp)
    #
    # f1.close()

    # compter le nombre de caractere du fichier
    # print(len(outp))

    # time.sleep(5)

    # EOF
    # print()
    time.sleep(2)

loop = asyncio.get_event_loop()
coro = telnetlib3.open_connection(server_ip, 23, shell=shell)
reader, writer = loop.run_until_complete(coro)

loop.run_until_complete(writer.protocol.waiter_closed)