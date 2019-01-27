# File Transfer client side
'''
Client always waiting to receive data from the server
'''

import socket

# open a socket connected to the server port
sock = socket.socket()
host = " 10.182.179.221" #$$$Enter local ip address of your computer$$$.
port = 8080

#host = input("Enter the ip address of the server that you wanna connect to: ")
#port = int(input("Enter the port of the server: "))

# request for the directory
sock.connect((host,port))
sock.send("which files do you have for me?".encode())


dirs = sock.recv(1024)
print (dirs.decode())

# select the file and send the choice to the server
#opt = input("Select which file you want to download\n")
#sock.send(opt.encode())


fpath = "G:\\Distributed Systems\\multithreading\\client2\\" # $$$ Enter the path to the client2 folder present on your computer$$$.

bsize = 1024	
# request for the directory
#sock.connect((host,port))

flcount = 0
print ('Waiting for data...')

while (flcount <=3):
	data = sock.recv(bsize)
	if "Sending file" in data.decode():
		ext = '.{0}'.format(data.decode().rsplit('.',1)[1])
		flname = '{0}{1}{2}{3}'.format(fpath,"newfile",str(flcount),ext)
		with open(flname,'wb') as f:
			print ('Getting new file...')
			sock.send("ok".encode())
			data = sock.recv(bsize)
			while data:
				if "eof" in data.decode("utf-8", "replace"):
					break
				else:
					f.write(data)
					sock.send("ok".encode())
					data = sock.recv(bsize)
		f.close()
		flcount = flcount + 1
		
