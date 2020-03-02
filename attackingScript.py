import sys
from scapy.all import *
print ("Packet Strucutre")
#Below code will generate TCP packets with SYN flag equals to 1
p=IP(src="192.168.2.27",dst=sys.argv[1],id=1111,ttl=99)/TCP(sport=RandShort(),dport=80,seq=12444,ack=1000,window=1000,flags="S")
ls(p)
print ("Sending packets")
ans,unans=srloop(p,inter=0.3,retry=2,timeout=4)
print ("Summary of packets sent")
ans.summary()
unans.summary()
# Below code will display the response of the packets sent above
print ("source port flags in response")
ans.make_table(lambda s,r: (s.dst, s.dport, r.sprintf("%IP.id% \t %IP.ttl% \t %TCP.flags%")))