
## capturing packets with scapy
## using sniff()  for capturing real time packets or traffic

from scapy.all import sniff
from packet_logger import process_packet
import threading 
import time



## adding the real time status of outoput

from protocol_statistics import update_stats, print_stats

def handle_packet(packet):
	process_packet(packet) ## logging details to file
	update_stats(packet) ## updates the protocol statictics

## prints output every 5 seconds

def stats_loop():
	while True:
		time.sleep(5)
		print("\n ***** Protocol Statistics are displaying below *****")
		print_stats()
		print("=" * 40)

if __name__ == "__main__":
	print("***** Starting the Network Traffic Analyzer *****")


	## starts stats printing thread
	stats_thread = threading.Thread(target=stats_loop, daemon=True)
	stats_thread.start()

	## starting  packet sniffing
	sniff(prn=handle_packet, store=False)
