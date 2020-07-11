#!/bin/python

import sys
import socket
from datetime import datetime

try:
	#Defining Target
	if len(sys.argv)==2:
		target = socket.gethostbyname(sys.argv[1])	#Translates Hostname to IPv4
	else:
		print("[-] Invalid Arguments !")
		print("Syntax	: python3 scanner.py <ip>")
		print("Example	: python3 scanner.py 127.0.0.1")
		sys.exit()

	#Banner
	print("-"*60)
	print("\t\tWelcome to V Port Scanner\n")
	print("\tScanning Target	: "+target)
	print("\tTime Started at	: "+str(datetime.now()))
	print("-"*60)
	
	for port in range(1,65535):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target, port))
		if result == 0:
			print("Port {} is open.".format(port))
		s.close()
		
except KeyboardInterrupt: 
	print("\nExiting...\n")
	sys.exit()
	
except socket.gaierror:
	print("[-] Hostname can't be resovled.")
	print("Example: python3 scanner.py 127.0.0.1")
	print("	 python3 scanner.py <domain_name>")
	sys.exit()

except socket.error:
	print("[-] Couldn't connect to Server.")
	sys.exit()
