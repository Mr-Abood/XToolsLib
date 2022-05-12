# XToolsLib
![](https://img.shields.io/badge/XToolsLib-orange?style=for-the-badge&logo=python.svg) 
<a href="https://t.me/O0OO2"><img title="Telegram" src="https://img.shields.io/badge/telegram%20-X | Tools-red.svg?style=for-the-badge&logo=telegram"></a>
## v0.1

## Installation

``` 
pip install XToolsLib
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
