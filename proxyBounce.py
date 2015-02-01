#!/usr/bin/python
import socket
import select
import time
import sys

# Changing the buffer_size and delay, you can improve the speed and bandwidth.
# But when buffer get to high or delay go too down, you can broke things
buffer_size = 4096
delay = 0.0001
#forward_to = ('192.168.239.128', 8888)

class Forward:
    def __init__(self):
	        self.forward = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self, host, port):
        try:
            self.forward.connect((host, port))
            return self.forward
        except Exception, e:
            print e
            return False

class TheServer:
    input_list = []
    channel = {}

    def __init__(self, host, port):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((host, port))
        self.server.listen(200)

    def main_loop(self):
        self.input_list.append(self.server)
        while 1:
            time.sleep(delay)
            ss = select.select
            inputready, outputready, exceptready = ss(self.input_list, [], [])
            for self.s in inputready:
                if self.s == self.server:
                    self.on_accept()
                    break

                self.data = self.s.recv(buffer_size)
                if len(self.data) == 0:
                    self.on_close()
                    break
                else:
                    self.on_recv()

    def on_accept(self):
        clientsock, clientaddr = self.server.accept()
        cloud_data=clientaddr[0]
        #print "Client address is"+ clientaddr
        forward= clientsock.recv(buffer_size)
        print forward
        try:
            remote_ip = socket.gethostbyname( '128.61.78.80' )
            print remote_ip
        except socket.gaierror:
	        #could not resolve
            print 'Hostname could not be resolved. Exiting'
            sys.exit()

        try:
            scloud = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error:
            print 'Failed to create socket'
            sys.exit()
       
        print "Socket to cloud created"

        host = '128.61.78.80';
        port = 4000;
 
        try:
            remote_ip = socket.gethostbyname( host )
 
        except socket.gaierror:
            #could not resolve
            print 'Hostname could not be resolved. Exiting'
            sys.exit()

        print "Host retrieved"
        scloud.connect((remote_ip , port))
        print 'Socket Connected to ' + host + ' on ip ' + remote_ip
        scloud.sendall(cloud_data)

        replyCloud = scloud.recv(4096)
        #scloud.close()
        print "REPLY IS"
        print replyCloud
        print type(replyCloud)
        if replyCloud == "no" :
            #scloud.close()
            print "BLOCKED!!!!!!!"
            sys.exit()
        else :
            print "Allowed"
            

        forward = Forward().start(remote_ip, 8888)	
        if forward:
            print clientaddr, "has connected"
            self.input_list.append(clientsock)
            self.input_list.append(forward)
            self.channel[clientsock] = forward
            self.channel[forward] = clientsock
        else:
            print "Can't establish connection with remote server.",
            print "Closing connection with client side", clientaddr
            clientsock.close()

    def on_close(self):
        print self.s.getpeername(), "has disconnected"
        #remove objects from input_list
        self.input_list.remove(self.s)
        self.input_list.remove(self.channel[self.s])
        out = self.channel[self.s]
        # close the connection with client
        self.channel[out].close()  # equivalent to do self.s.close()
        # close the connection with remote server
        self.channel[self.s].close()
        # delete both objects from channel dict
        del self.channel[out]
        del self.channel[self.s]

    def on_recv(self):
        data = self.data
        print data
        self.channel[self.s].send(data)
        # here we can parse and/or modify the data before send forward




if __name__ == '__main__':
        server = TheServer('128.61.78.80', 9090)
        try:
            server.main_loop()
        except KeyboardInterrupt:
            print "Ctrl C - Stopping server"
            sys.exit(1)
