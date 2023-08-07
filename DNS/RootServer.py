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
# This is the root server
serversocket = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
serversocket.bind((str(sys.argv[1]),int(sys.argv[2])))
while True:
    # takes input and checks if the domain is present in the root.txt 
    # if it is not present then it gives ERROR 404
    data,addr = serversocket.recvfrom(2048)
    data = data.decode().strip()
    filename = 'root.txt'
    # cheking if the domain is present in root.txt
    check = 0
    with open(filename,'r') as f:
        lines = f.readlines()

    found=''
    for line in lines:
        if(line[-1]=='\n'):
            line = line[:-1]
        temp = line.split()[0]
        if(temp.split('_')[1]==data):
            check = 1
            found = line
            msg = line.split()[1].strip()
    if check==0:
        msg ="ERROR 404"
    # Writing out outputs to required file
    o = open('rootOutput.txt','a+')
    o.write("recieved request : "+str(data))
    o.write('\n')
    o.write("found : "+str(found))
    o.write('\n')
    o.write("sending : "+msg)
    o.write('\n')
    o.write('****************************************')
    o.write('\n')
    o.close()
    serversocket.sendto(msg.encode(),addr)




