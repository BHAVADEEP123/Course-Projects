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
# crearing socket
serversocket = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
serversocket.bind((str(sys.argv[1]),int(sys.argv[2])))
while True:
    data,addr = serversocket.recvfrom(2048)
    domain = data.decode().split('.')
    filename = domain[1]+'.'+domain[2]+'.'+'txt'
    with open(filename,'r') as f:
        lines = f.readlines()
    # checking if the required domain is present or not
    # if not present the we send and error called "ERROR 404"
    check=0
    for line in lines:
        if(line[-1]=='\n'):
            line = line[:-1]
        temp = line.split()
        if(temp[0]==data.decode().strip()):
            check=1
            msg = temp[1]

    if check==0:
        msg ="ERROR 404"
    o = open('AuthOutput.txt','a+')
    o.write("recieved request : "+str(data.decode()))
    o.write('\n')
    o.write("sending : "+msg)
    o.write('\n')
    o.write('****************************************')
    o.write('\n')
    o.close()
    serversocket.sendto(msg.encode(),addr) 