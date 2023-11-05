import requests

url = "https://google.com"
resp = requests.get(url)
#print(dir(resp))
#print(resp.status_code)
if resp.status_code == 200:
    print("site is up and running")
else:
    print("Site is down")
