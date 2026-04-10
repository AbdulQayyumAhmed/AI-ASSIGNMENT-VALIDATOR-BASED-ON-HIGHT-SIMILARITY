import requests
API_BASE = "http://127.0.0.1:8000"
url = f"{API_BASE}/assignment-status"
print(f"Requesting: {url}")
try:
    r = requests.get(url, timeout=5)
    print(f"Status: {r.status_code}")
    print(f"Content-Type: {r.headers.get('Content-Type')}")
    print(f"Body: {r.text[:500]}")
except Exception as e:
    print(f"Error: {e}")
