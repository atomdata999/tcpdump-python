import sys
import os
ips = open(sys.argv[1], "r").readlines()   
for ip in ips:
	os.system(f"iptables -A INPUT -s {ip} -j DROP")
