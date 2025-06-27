# Network Traffic Analyzer

A lightweight Python-based tool for analyzing live network traffic and identifying potentially malicious IP addresses using the [AbuseIPDB API](https://abuseipdb.com). Built for cybersecurity learners, hobbyists, and network analysts to monitor packets and detect threats in real-time.




## Features

- **Live Packet Sniffing** using `scapy`
- **Real-time Packet Inspection** (source/destination IPs, ports, protocol, flags)
- **Threat Intelligence** with AbuseIPDB integration
- **Abuse Confidence Scoring** for IPs
- **Log Packet Data** for offline analysis
- **CLI Interface** for quick testing and learning


## Setup Instructions

### 1. 📥 Clone the Repository

```
git clone https://github.com/anonym-saurab/Network_Traffic_Analyzer.git
cd Network_Traffic_Analyzer
```


## Install Dependencies

```pip install -r requirements.txt```


##  Set Up AbuseIPDB API Key

> Sign up at AbuseIPDB

> Go to your dashboard and copy your API key

> Replace the placeholder in **test_abuseipdb.py**:

```
headers = {
    'Key': 'YOUR_API_KEY',
    'Accept': 'application/json'
}
```

## How to Use
> Run Packet Sniffer

```sudo python3 test_sniffer.py```
This will start sniffing your network interface and print packet details to the terminal.

> Check Reputation of a Specific IP

```sudo python3 test_abuseipdb.py```
You can modify the script to test **any IP address** by changing the ip variable in the script.

