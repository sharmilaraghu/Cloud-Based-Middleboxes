
class Firewall:
	iplist={}
	block="no"		
	accept="yes"
	def __init__(self, file_name_blacklist, file_name_white_list):
		self.iplist={}
		b = open(file_name_blacklist, 'r')
		for row in b:
			row=row.strip('\n')
			row=row.split()
			if(len(row)<2):
				continue

			if row[0] in self.iplist:
				print("Duplicate ip address: ", row[0])
				continue
			self.iplist[row[0]]=(row[1],self.block)

		w = open(file_name_white_list, 'r')
		for row in w:
			row=row.strip('\n')
			row=row.split(' ')
			if(len(row)<2):
				continue
			if row[0] in self.iplist:
				print("Duplicate ip address: ", row[0])
				continue
			self.iplist[row[0]]=(row[1],self.accept)


	def input_ip_port(self,ipaddress, port):
		if ipaddress in self.iplist:
			(dec_port, decision)=self.iplist[ipaddress]
			if dec_port=='*':
				return decision
			elif dec_port==port:
				return decision
		elif '*' in self.iplist:
			return self.iplist["*"][1]
		else:
			return self.block
	
	def input_ip(self,ipaddress):
		ipaddress=ipaddress.strip('\n\r\t ')
		if ipaddress in self.iplist:
			print "Ip "
			(dec_port, decision)=self.iplist[ipaddress]
			return decision
		elif '*' in self.iplist:
			return self.iplist["*"][1]
		else:
			return self.block

	def print_file(self):
		print("Self")
		for row in self.iplist:
			print(row)

if __name__ == "__main__":
	fire=Firewall('blackList.txt','whitelist.txt')
	fire.print_file()
	print(fire.input_ip("1.1.1.1" ))
	print(fire.input_ip("1.1.1.2"))
	print(fire.input_ip("1.1.1.4"))







