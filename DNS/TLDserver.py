# NAME: Bhavadeep Bhukya
# Roll No : cs20b015
# Course: CS3205 Jan. 2023 semester
# Lab number: 2
# Date of submission: 04-02-2023
# I confirm that the source file is entirely written by me without
# resorting to any dishonest means.
# Website(s) that I used for basic socket programming code are:
# URLs : https://www.geeksforgeeks.org/socket-programming-python/
import socket
import sys
import os

serversocket = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
serversocket.bind((str(sys.argv[1]),int(sys.argv[2])))
while True:
    data,addr = serversocket.recvfrom(2048)
    data = data.decode()
    tld = data.split('.')[-1]
    filename = tld+'.'+'txt'
    mainname = data.split('.')[-2]
    with open(filename,'r') as f:
        lines = f.readlines()
    check=0
    found = ''
    for line in lines:
        if(line[-1]=='\n'):
            line = line[:-1]
        temp = line.split()
        if(temp[0].split('.')[0]==mainname):
            found = line
            check=1
            msg = temp[1]
    if check==0:
        msg ="ERROR 404"
    o = open('TLDOutput.txt','a+')
    o.write("recieved request : "+str(data))
    o.write('\n')
    o.write("found : "+str(found))
    o.write('\n')
    o.write("Sending : "+msg)
    o.write('\n')
    o.write('****************************************')
    o.write('\n')
    o.close()
    serversocket.sendto(msg.encode(),addr)