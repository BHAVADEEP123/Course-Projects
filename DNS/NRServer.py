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
# server first takes TLD from given domain and seraches it in root database
n = len(sys.argv)
if(n!=3):
    nro = open("NR_OUTPUT.txt",'a+')
    nro.write("INPUT SEQUENCE IS WRONG")
    nro.write('\n')
    nro.write("*************************")
    nro.write('\n')
    nro.close()
else:
    
    pnos = open('portNumbers.txt','r')
    numbers = pnos.readlines()
    pnos.close()
    # print("hey")   
    serversocket = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
    serversocket.bind((str(sys.argv[1]),int(sys.argv[2])))
    while True:
        nro = open("NR_OUTPUT.txt",'a+')
        data,client_addr = serversocket.recvfrom(2048)
        data = data.decode().split()
        roothost = data[1]
        Port = int(data[-1])
        domainName = data[0]
        # split domain name
        togetTDS = domainName.split('.')[-1]
        togetADS = domainName.split('.')[-2]
        # calling root
        # server first takes TLD from given domain and seraches it in root database
        rootportno= ''
        for num in numbers:
            if 'root' in num and len(num.split())==2 :
                rootportno=int(num.split()[-1])
        # print(rootportno) 
        nro.write("sending request to root.. Request name : "+togetTDS) 
        nro.write("\n")      
        rootclient = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
        rootclient.sendto(togetTDS.encode(),(roothost,Port+rootportno))
        rootdata,rootaddr = rootclient.recvfrom(2048)
        if(rootdata.decode().strip()=="ERROR 404"):
            serversocket.sendto(rootdata,client_addr) 
            nro.write("Recieved msg from root : "+rootdata.decode())  
            nro.write('\n')
            nro.write("*************************")
            nro.write('\n')
            nro.close()
        else:
            # calling tldserver
            # Then NR calles TLD server to get ADS IP address 
            tldhost = rootdata.decode()
            tldclient = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
            tldportno = ''
            tempo = domainName.split('.')[-1]
            for num in numbers:
                if 'TDS' in num and tempo in num and len(num.split())==3:
                    tldportno=int(num.split()[-1])
            # print(tldportno)
            nro.write("sending request to TLD server.. Request name : "+domainName) 
            nro.write("\n") 
            tldclient.sendto(domainName.encode(),(tldhost,Port+tldportno))
            tldData,Tldaddr = tldclient.recvfrom(2048)
            if(tldData.decode().strip()=="ERROR 404"):
                serversocket.sendto(tldData,client_addr) 
                nro.write("Recieved msg from TLD Server : "+tldData.decode())  
                nro.write('\n')
                nro.write("*************************")
                nro.write('\n')
                nro.close()  
            else:
                # Then we search domain in ads and send report accordingly
                # calling ads server
                nro.write("sending request to ADS server.. Request name : "+domainName) 
                nro.write("\n") 
                domainclient = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
                adminportno = ''
                tempo = domainName.split('.')[-2]
                for num in numbers:
                    if 'ADS' in num and tempo in num and len(num.split())==3:
                        adminportno=int(num.split()[-1])
                # print(adminportno)
                adminhost = tldData.decode()
                domainclient.sendto(domainName.encode(),(adminhost,Port+adminportno))
                finaldata,addr = domainclient.recvfrom(2048)
                nro.write("Recieved msg from ADS : "+finaldata.decode())  
                nro.write('\n')
                nro.write("sending IP to system : "+finaldata.decode())
                nro.write('\n')
                nro.write("*************************")
                nro.write('\n')
                nro.close()
                serversocket.sendto(finaldata,client_addr)
                # serversocket.sendto(tldData,client_addr) 
                 
                




