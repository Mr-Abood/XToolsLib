# XToolsLib
![](https://img.shields.io/badge/XToolsLib-orange?style=for-the-badge&logo=python.svg) 
<a href="https://t.me/O0OO2"><img title="Telegram" src="https://img.shields.io/badge/telegram%20-X | Tools-red.svg?style=for-the-badge&logo=telegram"></a>
[![Telegram](https://img.shields.io/badge/Telegram-X|Tools-red?style=for-the-badge&logo=Telegram)](https://t.me/O0OO2)
[![Github](https://img.shields.io/badge/Github-Mr.Abood-red?style=for-the-badge&logo=github)](https://github.com/Mr-Abood)
## v0.1

## Installation

``` 
pip install XToolsLib
``` 

### Check Yahoo Email

``` python
import XToolsLib as XT

email = ""

#proxy = "IP:PORT"
#type = "http" or "https" or "socks4" or "socks5"
proxy = None
type = None

timeout = 10

Check = XT.MailChecker().Yahoo(email, proxy, type, timeout)
if Check:
	print("Available")
else:
	print("Unavailable")
``` 

### Check Outlook Email

``` python
import XToolsLib as XT

email = ""

#proxy = "IP:PORT"
#type = "http" or "https" or "socks4" or "socks5"
proxy = None
type = None

timeout = 10

Check = XT.MailChecker().Outlook(email, proxy, type, timeout)
if Check:
	print("Available")
else:
	print("Unavailable")
``` 

### Check Hotmail Email

``` python
import XToolsLib as XT

email = ""

#proxy = "IP:PORT"
#type = "http" or "https" or "socks4" or "socks5"
proxy = None
type = None

timeout = 10

Check = XT.MailChecker().Hotmail(email, proxy, type, timeout)
if Check:
	print("Available")
else:
	print("Unavailable")
``` 

### Check Gmail Email

``` python
import XToolsLib as XT

email = ""

#proxy = "IP:PORT"
#type = "http" or "https" or "socks4" or "socks5"
proxy = None
type = None

timeout = 10

Check = XT.MailChecker().Gmail(email, proxy, type, timeout)
if Check:
	print("Available")
else:
	print("Unavailable")
``` 

### Check Mail.ru Email

``` python
import XToolsLib as XT

email = ""

#proxy = "IP:PORT"
#type = "http" or "https" or "socks4" or "socks5"
proxy = None
type = None

timeout = 10

Check = XT.MailChecker().Mailru(email, proxy, type, timeout)
if Check:
	print("Available")
else:
	print("Unavailable")
```

### Check Aol Email

``` python
import XToolsLib as XT

email = ""

#proxy = "IP:PORT"
#type = "http" or "https" or "socks4" or "socks5"
proxy = None
type = None

timeout = 10

Check = XT.MailChecker().Aol(email, proxy, type, timeout)
if Check:
	print("Available")
else:
	print("Unavailable")
``` 

### Create Fake Mail

``` python
import XToolsLib, time

m = []

fm = XToolsLib.FakeMail()
email = fm.Create()

print("Your mail is : "+email)
print("_____________________\n")
while True:
	time.sleep(5)
	msg = fm.Messages()
	if len(msg) != 0 and not msg[0] in m:
		mm = msg[0]
		print("New message 📧")
		print("_____________________")
		print(f"Email : {mm['from']['address']}")
		print(f"Name : {mm['from']['name']}")
		print(f"Subject : {mm['subject']}")
		print(f"Message : {mm['message']}")
		print(f"Date : {mm['date']}")
		print("_____________________\n")
		m.append(mm)	
```

### Contact
Telegram : [Mr.Abood](https://t.me/O0O0I)

Channel : [X | Tools](https://t.me/O0OO2)

Email : XTools@outlook.sa

Project Link : https://github.com/Mr-Abood/XToolsLib
