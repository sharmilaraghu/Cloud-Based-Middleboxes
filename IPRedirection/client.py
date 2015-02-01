#Socket client example in python
 
import socket   #for sockets
import sys  #for exit
 
#create an INET, STREAMing socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print 'Failed to create socket'
    sys.exit()
     
print 'Socket Created'
 
host = '128.61.78.80';
port = 9090;
 
try:
    remote_ip = socket.gethostbyname( host )
 
except socket.gaierror:
    #could not resolve
    print 'Hostname could not be resolved. Exiting'
    sys.exit()
 
#Connect to remote server
s.connect((remote_ip , port))
 
print 'Socket Connected to ' + host + ' on ip ' + remote_ip
#reply = s.recv(4096)
#Send some data to remote server
#message = raw_input('Enter your destination website:')
message = '128.61.125.216'
destination_ip = socket.gethostbyname( message )
print "Starting server communication"
start_time = time.time()
print "Start time is"
print start_time
for i in range(100)
    try :
        #Set the whole string
        s.sendall(destination_ip)
        reply = s.recv(4096)
    except socket.error:
        #Send failed
        print 'Send failed'
        sys.exit()
 print 'Communicated successfully'
end = time.time()
print "End time is"
print end
diff = end - start
print "Time taken ="
print diff
#while 1:
#	message=raw_input('Send more?')
#	s.sendall(message)
	#Now receive data
#	reply = s.recv(4096)
#	print reply
 	
