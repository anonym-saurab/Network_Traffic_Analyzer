from scapy.layers.inet import IP, TCP, UDP
from abuse_lookup import is_malicious_ip

def process_packet(packet):
	if IP in packet:
		ip_layer = packet[IP]
		src_ip = ip_layer.src
		dst_ip = ip_layer.dst

		if TCP in packet:
			protocol = "TCP"
		elif UDP in packet:
			protocol = "UDP"
		else:
			protocol = str(ip_layer.proto) ## here  comes the fallback

		## printing in the comsole
		print(f"{src_ip} -> {dst_ip} | Protocol: {protocol}")

		## real time AbuseIPDB check
		if is_malicious_ip(dst_ip) or is_malicious_ip(src_ip):
			print(f"[Real Time Alert !] Malicious IP Detected: {src_ip} -> {dst_ip}")

		## logging the details
		with open("traffic_log.txt", "a") as f:
			f.write(f"{src_ip} -> {dst_ip} | Protocol: {protocol}\n")

