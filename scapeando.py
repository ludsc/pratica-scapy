from scapy.all import *
import numpy as np

pcap_p = rdpcap("video_traffic.pcap")

#hexdump(pcap_p[0])
#pcap_p[0].show()
#pcap_p[0].canvas_dump()
tcp_pacotes = []
timestamps = []
jitter_valores = []
for frame in pcap_p:
    if frame.haslayer("TCP"):
        timestamps.append(frame.time)
        tcp_pacotes.append(frame)
 
for i in range(1, len(timestamps)-1 ):
    jitter = timestamps[i] - timestamps[i-1]
    jitter_valores.append(float(jitter))

jitter_media = np.mean(jitter_valores)
    
print(f"Feito o filtro, pacotes capturados: {len(tcp_pacotes)}")
print(f"Feito o filtro, o tamanho de timestamps é: {len(timestamps)}")
print(f"Média do jitter é: {(jitter_media)} segundos")