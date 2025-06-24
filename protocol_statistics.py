## creating the statictics dashbard

protocol_counter = {"TCP": 0, "UDP": 0, "ICMP": 0, "Other": 0}

def update_stats(packet):
	from scapy.layers.inet import TCP, UDP, ICMP
	if TCP in packet:
		protocol_counter["TCP"] += 1
	elif UDP in packet:
		protocol_counter["UDP"] += 1
	elif ICMP in packet:
		protocol_counter["ICMP"] += 1
	else:
		protocol_counter["Other"] += 1

def print_stats():
	print("***** Protocol Statistics *****")
	for proto, count in protocol_counter.items():
		print(f"{proto}: {count}")

