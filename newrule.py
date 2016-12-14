import random
import re

def act():
	lst = ['alert','log','pass']
	action = raw_input("type of action: alert, log, pass\n")
	if action not in lst:
		print "plz enter a valid action"
		action = ""
		act()
	else:
		print "the entered actoin is: "+action
		return action
		
def proto():
	lst = ['tcp','icmp','udp']
	pro = raw_input("type of protocol: tcp, icmp , udp \n")
	if pro not in lst:
		print "plz enter a valid protocol"
		proto()
	else:
		print "the entered protocol is:"+pro
		return pro
def sip():
	ip = raw_input("plz enter the ip addr\n")
	aa = re.match(r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$",ip)
	if aa:
		return ip
	elif ip == 'any':
		return ip
	else:
		print "plz insert a valid ip"
		sip()
		
def sport():
	port = raw_input("plz enter the source port \n")
	if port.isdigit():
		if int(port) > 0 and int(port) < 65536:
			return port
	elif port == 'any':
		return port
	else:
		print "plz enter a valid port number"
		sport()
def dip():
	ip = raw_input("plz enter the source port \n")
	aa = re.match(r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$",ip)
	if aa:
		return ip
	elif ip == 'any':
		return ip
	else:
		print "plz insert a valid ip"
		dip()
def dport():
	port = raw_input("plz enter the source port \n")
	if port.isdigit():
		if int(port) > 0 and int(port) < 65536:
			return port
	elif port == 'any':
		return port
	else:
		print "plz enter a valid port number"
		dport()
def getmsg():
	msg = raw_input("plz enter the message for alert/log \n")
	return msg
def getsid():
	s = random.randint(1000000, 10000000)
	return s
	
def main():
	action = act()
	pro = proto()
	sips = sip()
	sports = sport()
	dips = dip()
	dports = dport()
	msg = getmsg()
	num = getsid()
	rule = action+" "+pro+" "+sips+" "+sports+" -> "+dips+" "+dports+" (msg:"+msg+";sid:"+str(num)+";)"
	print rule
	nm = raw_input("plz provide the filename you want to insert the rule: \n")
	f = open(nm,'a')
	f.write("\n"+rule)
	f.close()
	if__name__=="__main__":
		main()
	
	