from googlevoice import Voice
from googlevoice.util import input
import time

voice = Voice()


user_info = open('user_info.txt', 'r')
user_name = user_info.readline()
user_pass = user_info.readline()
user_info.close()
voice.login(user_name, user_pass)


try:
	phoneNumber = '5172902947'
	text = 'Hello, World!'
except:
	voice.login()
finally:
	voice.send_sms(phoneNumber, text)