class Requests():
	def __init__(self, url, headers, data, proxy, proxy_type, timeout):
		import requests
		if not proxy == None and not proxy_type == None:
			if proxy_type == "http":
				proxies = {'http' : f"http://{proxy}",'https' : f"https://{proxy}"}
				res = requests.post(url, headers=headers, data=data, timeout=timeout, proxies=proxies)
			elif proxy_type == "https":
				proxies = {'http' : f"http://{proxy}",'https' : f"https://{proxy}"}
				res = requests.post(url, headers=headers, data=data, timeout=timeout, proxies=proxies)
			elif proxy_type == "socks4":
				proxies = {'http' : f"socks4://{proxy}",'https' : f"socks4://{proxy}"}
				res = requests.post(url, headers=headers, data=data, timeout=timeout, proxies=proxies)
			elif proxy_type == "socks5":
				proxies = {'http' : f"socks5://{proxy}",'https' : f"socks5://{proxy}"}
				res = requests.post(url, headers=headers, data=data, timeout=timeout, proxies=proxies)
			else:res = requests.post(url, headers=headers, data=data, timeout=timeout)
		else:res = requests.post(url, headers=headers, data=data, timeout=timeout)
		self.text = res.text
		self.status_code = res.status_code
		try:self.json = res.json()
		except:pass
		self.content = res.content
		self.headers = res.headers
		self.cookies = res.cookies
