# test_abuseipdb.py
import requests

API_KEY = "01dd2d19697bbe2ff18a219a59c1abae816311786806721de249fbd8d0b2d369aca2c0c6d7feeaaa"

def test_ip(ip):
    url = "https://api.abuseipdb.com/api/v2/check"
    headers = {
        "Key": API_KEY,
        "Accept": "application/json"
    }
    params = {
        "ipAddress": ip,
        "maxAgeInDays": 90
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        print("Abuse Score:", data["data"]["abuseConfidenceScore"])
    except Exception as e:
        print("[ERROR] AbuseIPDB request failed:", e)

test_ip("3.233.158.26")  # Example IP

