class FakeMail():
	def Create(self):
		import requests, json, random
		nm=0
		while nm == 0:
			api_address = "https://api.mail.tm"; r = requests.get("{}/domains".format(api_address)); response = r.json();domains = list(map(lambda x: x["domain"], response["hydra:member"]));address = str("".join(random.choice('qwertyuiopasdfghjklzxcvbnm1234567890') for i in range(16)))+"@"+str(random.choice(domains)); password = "dbusejjdsj"; account = {"address": address, "password": password}; headers = {"accept": "application/ld+json","Content-Type": "application/json"}; r = requests.post("{}/accounts".format(api_address),data=json.dumps(account), headers=headers)
			if int(r.status_code) == 201:nm+=1;self.email = r.json()["address"]; self.token = requests.post("https://api.mail.tm/token",data=json.dumps({"address": r.json()["address"], "password": password}), headers=headers).json()["token"];return self.email
	def Messages(self):
		import requests
		try:
			response, messages, ll = requests.get("https://api.mail.tm/messages", headers={"accept": "application/ld+json","Content-Type": "application/json","Authorization": "Bearer {}".format(self. token)}).json()["hydra:member"], [], lambda msg: messages.append({"from":msg["from"],"subject":msg["subject"],"message":msg["intro"],"date":msg["createdAt"]})
			if len(response)==0:return []
			for msg in response:ll(msg);return messages
		except AssertionError:raise Exception("First, create an email.")