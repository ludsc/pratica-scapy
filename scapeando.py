import sys
from scapy.all import *

pcap_p = rdpcap("video_traffic.pcap")

#hexdump(pcap_p[0])
#pcap_p[0].show()
#pcap_p[0].canvas_dump()