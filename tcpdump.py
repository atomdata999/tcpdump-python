import os
import sys
from colorama import Fore, Style
print(f"{Fore.BLUE}Dumping Started")
os.system("tcpdump -c 100000 -w lol.pcap")
os.system("tshark -i - < ""lol.pcap"" > ""output.txt""")
os.system("cat output.txt | awk {'print $3'} | sort | uniq -d >> bots.txt")
os.system("python3 blacklist.py bots.txt")
