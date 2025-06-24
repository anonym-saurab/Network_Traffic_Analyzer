import requests

API_KEY = "01dd2d19697bbe2ff18a219a59c1abae816311786806721de249fbd8d0b2d369aca2c0c6d7feeaaa"

def is_malicious_ip(ip):
	url = "https://api.abuseipdb.com/api/v2/check"
	headers = {"key": API_KEY, "Accept": "application/json"}
	params = {"ipaddress": ip, "maxAgeInDays": 90, "verbose": True}

	try:
		response = requests.get(url, headers=headers, params=params)
		data = response.json()

		if "data" in data:
			score = data["data"]["abuseConfidenceScore"]
			return score >= 50 ## we can adjust this threshold
		else:
			return False
	except Exception as e:
		print(f"[ERROR] AbuseIPDB request failed: {e}")
		return False
