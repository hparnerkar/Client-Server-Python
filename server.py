# File transfer server side
'''

Program for server multithreading
Allows massive transfer from a specific folder in the server side to another folder in the client

'''

import socket
import os, sys
import threading
import time
#import SocketServer

# Main variables and constants
port = 8080
host = " 10.182.179.221" # $$$ Enter the local IP address of your computer $$$.
fpath = "G:\\Distributed Systems\\multithreading\\server\\" # $$$Enter the path to the folder where the server folder is placed on your computer$$$.
bsize = 1024

class mainServer(object):

    def __init__(self,host,port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        host = socket.gethostname()
        self.sock.bind((host,port))
        self.sock.listen(5)
        print ('Server Ready...')
        self.runServer()
        self.delete()

    def runServer(self):
        # loop to get a connection
        while True:
            print ("waiting for connections...")
            (conn, (ip,port)) = self.sock.accept()
            conn.settimeout(360)

            threading.Thread(target = ServerThread, args = (conn,ip,port)).start()
            time.sleep(40)
            '''if input() == "q":
                break'''
        

       
                

    
class ServerThread(object):
    
    def __init__(self,conn,ip,port):
        self.ip = ip
        self.port = port
        print ('{0}-{1}:{2}'.format("New client connected",str(ip),str(port)))
        #self.runThread(conn,'{0}:{1}'.format(str(ip),str(port)))
        c=input("do you want to delete files from server Press Y or N\n") #Delete Operation
        if(c=='Y'):
                for root, dirs, files in os.walk(fpath):
                     for file in files:
                         print("File = %s" % file)
                delfile= input("enter the name of file you want to delete along with extension\n")        
                os.remove("G:\\File transfer\\multithreading\\server\\"+delfile) #$$$Enter the path to the folder where the server folder is placed on your computer$$$.
                print("file deleted\n")
        else:
            print("file not deleted")
        x=input("Do you want to rename your file?!! Press Y or N\n") #Rename Operation
        if(x=='Y'):
            for root, dirs, files in os.walk(fpath):
                     for file in files:
                         print("File = %s" % file)
            prevname=input("Enter the name of the file you want to rename from above ?!!\n")
            newname=input("Enter the new  name of the file along with extension!!\n ")
            os.rename("G:\\File transfer\\multithreading\\server\\"+prevname,"G:\\File transfer\\multithreading\\server\\"+newname) #$$$Enter the path to the folder where the server folder is placed on your computer$$$.
            print("file renamed")
        else:
            print("not renamed")
        self.runThread(conn,'{0}:{1}'.format(str(ip),str(port)))

    def runThread(self,conn,addr):
        
            z=input("Do you want to dowanload? Press Y or N\n") #Download Operation
            if(z=='Y'):
                flcount=0
                while True:
                    
                    dirs = os.listdir(fpath)
                    time.sleep(10)
                    for fl in dirs:
                            msg = '{0}{1}'.format("Sending file: ",fl)
                            conn.send(msg.encode())
                            if "ok" in conn.recv(bsize).decode(): # client ready to receive
                                    selfl = '{0}{1}'.format(fpath,fl)
                                    f = open(selfl,'rb')
                                    payload = f.read(bsize)
                                    while (payload):
                                            conn.send(payload)
                                            print('\n........\n')
                                            if "ok" in conn.recv(bsize).decode():
                                                payload = f.read(bsize)
                                    conn.send("eof".encode())
                                    f.close()
                    
            else:
                print("Download cancelled\n")
       
  
        
                   
srv = mainServer(host,int(port))

