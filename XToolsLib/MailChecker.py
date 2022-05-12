class MailChecker():
	@staticmethod
	def Yahoo(email, proxy=None, type=None, timeout=1000):
		from urllib.parse import urlencode
		from XToolsLib.Requests import Requests
		if email == "" or not "@" in email:return False
		mail = str(email).split("@")[0]
		head = {
			'Host':'login.yahoo.com',
			'Connection':'keep-alive',
			'Content-Length':'18171',
			"Origin": "https://login.yahoo.com",
			'X-Requested-With': 'XMLHttpRequest',
			'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; Griffe T2 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.84 Mobile Safari/537.36',
			'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
			'Accept':'*/*',
			'Referer': 'https://login.yahoo.com/',
			'Accept-Encoding': 'gzip, deflate',
			'Accept-Language': 'ar-DZ,en-US;q=0.9',
			'Cookie': 'AS=v=1&s=tR1afqgt'
		}
		data={
			"language":"ar-DZ",
			"colorDepth":32,"deviceMemory":"unknown",
			"pixelRatio":1.7000000476837158,
			"hardwareConcurrency":4,
			"timezoneOffset":-60,
			"timezone":"Africa/Brazzaville",
			"sessionStorage":1,"localStorage":1,
			"indexedDb":1,"openDatabase":1,
			"cpuClass":"unknown",
			"platform":"Linux armv7l",
			"doNotTrack":"unknown",
			"plugins":{"count":0,
			"hash":"24700f9f1986800ab4fcc880530dd0ed"},
			"canvas":"canvas winding:yes~canvas",
			"webgl":1,
			"webglVendorAndRenderer":"ARM~Mali-400 MP",
			"adBlock":0,
			"hasLiedLanguages":0,"hasLiedResolution":0,"hasLiedOs":0,
			"hasLiedBrowser":0,"touchSupport":{"points":2,"event":1,"start":1},
			"fonts":{"count":11,"hash":"1b3c7bec80639c771f8258bd6a3bf2c6"},"audio":"124.08072748804261",
			"resolution":{"w":"424","h":"753"},
			"availableResolution":{"w":"753","h":"424"},
			"ts":{"serve":1626712821242,"render":1626712819533}
		}
		url = "https://login.yahoo.com/account/module/create?validateField=passwor"
		ur = f"&specId=yidreg&cacheStored=&crumb=g4rpM.Igx0K&acrumb=tR1afqgt&done=https://mail.yahoo.com/m/?.intl=xa&.lang=ar&firstName=mrabood&lastName=mrabood&yid={mail}&password=mraboodyahoo&shortCountryCode=US&phone=15046844748&mm=2&dd=3&yyyy=200&freeformGender=U&signup=&signup";
		data = urlencode(data)+ur
		resp = Requests(url=url, data=data, headers=head, proxy=proxy, proxy_type=type, timeout=timeout)
		if not ('IDENTIFIER_NOT_AVAILABLE' in resp.text or 'IDENTIFIER_EXISTS' in resp.text ) and resp.status_code == 200:return True
		else:return False
	@staticmethod
	def Hotmail(email, proxy=None, type=None, timeout=1000):return MailChecker.Outlook(email, proxy, type, timeout)
	@staticmethod
	def Outlook(email, proxy=None, type=None, timeout=1000):
		from XToolsLib.Requests import Requests
		if email == "" or not "@" in email:return False
		url = "https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress=" + email + "&_=1604288577990"
		data = ''
		headers = {
		"Accept": "*/*",
		"Content-Type": "application/x-www-form-urlencoded",
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
		"Connection": "close",
		"Host": "odc.officeapps.live.com",
		"Accept-Encoding": "gzip, deflate",
		"Referer": "https://odc.officeapps.live.com/odc/v2.0/hrd?rs=ar-sa&Ver=16&app=23&p=6&hm=0",
		"Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
		"canary": "BCfKjqOECfmW44Z3Ca7vFrgp9j3V8GQHKh6NnEESrE13SEY/4jyexVZ4Yi8CjAmQtj2uPFZjPt1jjwp8O5MXQ5GelodAON4Jo11skSWTQRzz6nMVUHqa8t1kVadhXFeFk5AsckPKs8yXhk7k4Sdb5jUSpgjQtU2Ydt1wgf3HEwB1VQr+iShzRD0R6C0zHNwmHRnIatjfk0QJpOFHl2zH3uGtioL4SSusd2CO8l4XcCClKmeHJS8U3uyIMJQ8L+tb:2:3c",
		"uaid": "d06e1498e7ed4def9078bd46883f187b",
		"Cookie": "xid=d491738a-bb3d-4bd6-b6ba-f22f032d6e67&&RD00155D6F8815&354"}
		res = Requests(url=url, data=data, headers=headers, proxy=proxy, proxy_type=type, timeout=timeout)
		if 'Neither' in res.text:
			return True
		else:
			return False
	@staticmethod
	def Mailru(email, proxy=None, type=None, timeout=1000):
		from XToolsLib.Requests import Requests
		if email == "" or not "@" in email:return False
		import requests
		headers = {
			"Accept": "application/json, text/plain, */*",
			"Accept-Encoding": "gzip, deflate, br",
			"Accept-Language": "ar-PS,ar;q=0.9,en-US;q=0.8,en;q=0.7",
			"Connection": "keep-alive",
			"Content-Length": "371",
			"Host": "auth.mail.ru",
			"Origin": "https://account.mail.ru",
			"User-Agent": "Mozilla/5.0 (Linux; Android 10; BLA-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.48 Mobile Safari/537.36"
		}
		data = {
			"login": email,
			"htmlencoded": "false",
			"referrer": "https://mail.ru/",
			"email": email
		}
		res = Requests(url="https://auth.mail.ru/api/v1/pushauth/info", data=data, headers=headers, proxy=proxy, proxy_type=type, timeout=timeout)
		if int(res.json["status"]) == 200 and res.json["body"]["exists"] == False:
			return True
		else:
			return False
	@staticmethod
	def Gmail(email, proxy=None, type=None, timeout=1000):
		from XToolsLib.Requests import Requests
		if email == "" or not "@" in email:return False
		url = 'https://accounts.google.com/_/signup/accountdetails?hl=ar&_reqid=542235&rt=j'
		headers = {'google-accounts-xsrf': '1','user-agent': 'Mozilla/5.0 (Linux; Android 10; BLA-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.48 Mobile Safari/537.36'}
		data = {
			'continue': 'https://accounts.google.com/ManageAccount?nc=1',
			'f.req': '["AEThLlzjMe-lH_JVt0umUOb9JB1k6FY7RxzCV7w9rMAlVchZhcbkI0YpE0CA0SOBScO5xP1lDGXMijqbtPFFfdoyjDrxZWyk1B9gv24Y7gq9OambwYl0kQgtQhHGUBF3tfG8U9l1YDvOsOUhPrAt_O0IaLi24Bp1MFv34wuwRpFBt0yrjht2e__6BVk4xbtAL3xYk0jCjL0kTTBf-u1F1syWSZauJHHGzA","Abood","Aboood","Abood","Aboood","'+email.split("@")[0]+'","xtoolslib2022","'+email.split("@")[0]+'",true,1,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[],null,null,null,null,[]]]',
			'azt': 'AFoagUULkAlwlIeMKxnFTqgBwTj3bPF3-A:1652345024057',
			'cookiesDisabled': 'false',
			'deviceinfo': '[null,null,null,[],null,"PS",null,null,null,"GlifWebSignIn",null,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[],null,null,null,null,[]],null,null,null,null,1,null,false,1,""]',
			'gmscoreversion': 'undefined'
        }
		try:
			res = Requests(url=url, data=data, headers=headers, proxy=proxy, proxy_type=type, timeout=timeout).text
			if '[[["gf.wadr",3,"' in res:return True
			else:return False
		except:return False
	@staticmethod
	def Aol(email, proxy=None, type=None, timeout=1000):
		from XToolsLib.Requests import Requests
		if email == "" or not "@" in email:return False
		headers = {
            'Cookie': 'AS=v=1&s=RMpErDTP&d=A627e226e|RBRHaFn.2SqxmVjVYN4IbsQC1GbKaEUD2U0cv_17VlevFMeGn8Wv.ovGm3aJZM5a96fOmS1YHQ0kYeZ328mSzUmB1UAvg7x4UtNBGHdkxCywraNOuPHz_HhxpDmHOOMSmP2kXLfV_IvL7x7kuLNtsCvtSrI8M5FXPhF4jnNJzQBm_X4aPXL.8moswewudrdjhHersL87yZDgxlZMckuW7y5u_uwD9iX8kKbG9bg6IXFvCfH1GUbYexyYk9_lw6qpUmrSjGpZn1SgXzWM.ZkzGElFu5tBetBWqu.Wz.ehnyekKmp.OOjESd_xgzh4kwsWNyhQH5eyf3lpHr17_wMj9Ae7QfwYcAc72n_xnfibnWKWSbL8TFXbjCUaWr78SaItN8iv3WLh27k30FyyabwpuyLFJlTqL5OXzXKChaA3tygjJzL9IgsrlpTR52_tLq8NtMjmqoLDP6SKG7JZdsVDeSKlZONngGF7qdsArycGK.MtIuUP9JjsHG5M8AsPpubxdecJwrDW6AvvLO0kihllCvfcdPUONn8OBz.xxamKiHuw2QvJERKSutFRRVM7CbU1Mrw9g5WzswzjJNYyp8ZZGLW.k48WOlVv4foy7OrcUxTvKMzf1G4ELk.pRe16289GnK5iUR1jtR.ytBLUO9NwrQiL2B95TlJsrmDYTtamaUkhbojejSnu2MMcEchJJZU4399LwW6njGtFXT1QFv_cMBHlLb0P9.9QTR4u9uI.emiQBuABdTEmYDruy1e3kRnWo9BUQ_XftibzGgQoVo2kSJv4gKIAJ_fWCcRcWbGfMC.i4KXketjzTOElsRy.1gN5FJaPBtyS6hnickawSQvibXC1BoyuVWOPHFu5d.UYNdxUxuecS1.fswd3Ac0xfDMEimuqdAtg83_O1kFOBPtTa80PwyW4W59GacJMunyWz7K2Q5BWNW..G3H0cjDk1ivDRJMVCBr5IFjOWW7eONXqoj3_r6j_HKe8Y4URSfe2Qw--~A|B627e226e|WYPSFhP.2SqcTfmHWdAOz782B5ysF9wQ_qGAStXIwDgOBWkAMC3Mwsv.cFUSq70GrFejCqNQPfRNCLKYBIWek.0kTptR0CyM.9bqxpJYp1k78ZW_S8XojZnu0j0ApKWUOGYgezh0.jLcYCK1ZbJWIT98UGXINWpn4p5D0rOOS90PZJBHvooax.5SEJ1OPQhb9bATVVmjoNiYeDkRsQfPFQIlVn3IJljS3PlPIv7O_QC2x9sbZipT3TCgD0XlKvJiN0yL11_ME4_iKBHS.gnBQBmQ9W_ItGGleFhF_SzJqazaRkdyUv1BKEXQ9NOgGZD_2OvS6ltrzwwS62EiLBRhMYFfZmKfdHRbfjS1xAmQYaSNGn8blFGqyTglhk6Vx6f0PXZYoHLn5WI4Z6XtVpAo13mG7KvMTdbDq8d6WLjp1.6DdxCjuKsYWZ_iSQdTwvPZ6p7JxA..udxYB7avI6TnEOGPykj0Pepnv2kwOrVbShflNQnqxAS5RLxveVINzSM8qippITyGAb9YuJrixK07MtJ9DshWzGxfN7wQq_3bdT_7OuLliZfqRxbmp5UYvt_lVWrg_iFfBoE5RoHQxSE9Qp5mHgUA_PdVaaq8ODu8bF9PBSB9gUy9h47.6oKlBW8TZ2f7oTKloccxfiiR8yWa6a3u9owrsaRKqNNBzRCYMd6ld9hHpGOfcm9UHKo.Ds.Zq.LgjiFJwKh8nsjJa.UQyEEy98dANam2TY2_rH_j4vE2GSkMuT1fTUKtdYRGwokmJ5kS9DVY3Ea768bxr.dPvpXzn4r5MoHohHO3ce._6gA8UlaDQVUFmQ.xq07cXRAFrtW4zVT3PUlYLF6arjE65mzn4Guv7V91crdzqc36_b.np6IE8k3pCEv__9r.JfoKo79xhr1wEkbijP4ADUc6qHOUaLkVw_KRMXHjRXGHufAsR1O0TM5D7vPwUMW.Tj9DMfMNQy0_gKv.4LbLLg2p_2lY64gKmDrp4selVls8yIxQ~A',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; BLA-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.48 Mobile Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
        }
		data = {
			'browser-fp-data': '{"language":"ar-PS","colorDepth":24,"deviceMemory":4,"pixelRatio":3,"hardwareConcurrency":8,"timezoneOffset":-180,"timezone":"Asia/Jerusalem","sessionStorage":1,"localStorage":1,"indexedDb":1,"openDatabase":1,"cpuClass":"unknown","platform":"Linux aarch64","doNotTrack":"unknown","plugins":{"count":0,"hash":"24700f9f1986800ab4fcc880530dd0ed"},"canvas":"canvas winding:yes~canvas","webgl":1,"webglVendorAndRenderer":"ARM~Mali-G72","adBlock":0,"hasLiedLanguages":0,"hasLiedResolution":0,"hasLiedOs":0,"hasLiedBrowser":0,"touchSupport":{"points":5,"event":1,"start":1},"fonts":{"count":11,"hash":"1b3c7bec80639c771f8258bd6a3bf2c6"},"audio":"124.08072766105033","resolution":{"w":"360","h":"720"},"availableResolution":{"w":"720","h":"360"},"ts":{"serve":1652347118533,"render":1652347118945}}',
			'crumb': 'jNKWFBfHm7N',
			'acrumb': 'RMpErDTP',
			'sessionIndex': 'Qg--',
			'displayName': '',
			'deviceCapability': '{"pa":{"status":true}}',
			'username': email,
			'passwd': '',
			'signin': 'Next'
        }
		res = Requests(url="https://login.aol.com/", data=data, headers=headers, proxy=proxy, proxy_type=type, timeout=timeout).text
		if "Sorry, we don't recognize this email." in res:return True
		else:return False