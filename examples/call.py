from googlevoice import Voice
from googlevoice.util import input


voice = Voice()

try:
	user_info = open('user_info.txt', 'r')
	user_name = user_info.readline()
	user_pass = user_info.readline()
	voice.login(user_name, user_pass)
	outgoingNumber = '5172902947'
	forwardingNumber = '0000000000'
	user_info.close()
except:
	voice.login()
finally:
	voice.call(outgoingNumber, forwardingNumber)

if input('Calling now... cancel?[y/N] ').lower() == 'y':
    voice.cancel(outgoingNumber, forwardingNumber)

