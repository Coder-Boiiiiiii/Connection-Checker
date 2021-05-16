import requests

url = str(input("URL: "))
timeout = 5

try:
	request = requests.get(url, timeout=timeout)
	print("You are connected to the Internet.")
  
except (requests.ConnectionError, requests.Timeout) as exception:
	print("You are not connected to the Internet.")
