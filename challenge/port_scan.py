import sys
import socket
def Check_Valid_ip(ip):
	addr=ip.split('.')
	if len(addr) == 4:
		try:
			socket.inet_aton(ip)
			return True
		except:
			return False
	else:
		return False
def Scan_Port(ip,port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	ip_status=Check_Valid_ip(ip)
	if ip_status:
		port_length=port.split('-')
		if len(port_length) ==2:
			for ports in range(int(port_length[0]),int(port_length[1])+1):
				result=sock.connect_ex((ip,ports))
				if result == 0:
					print("Port %d is open" % ports)
				else:
					print("Port %d is close" % ports)
		elif len(port_length) == 1:
			result=sock.connect_ex((ip,int(port)))
			if result == 0:
					print("Port %s is open" % port)
		else:
			print "pease like port-port or port type"
	else:
		print("invalid ip")
		sys.exit()	

if __name__ == '__main__':
	if len(sys.argv) == 3:
		host_ip=sys.argv[1]
		host_port=sys.argv[2]	
		Scan_Port(host_ip,host_port)
	else:
		print "python port_scan.py [IP] [PORT]"
