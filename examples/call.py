from googlevoice import Voice


voice = Voice()

try:
	user_info = open('user_info.txt', 'r')
	user_name = user_info.readline()
	user_pass = user_info.readline()
	voice.login(user_name, user_pass)
	outgoingNumber = '2697497663'
	forwardingNumber = '5172902947'

	user_info.close()
except:
	voice.login()

voice.call(outgoingNumber, forwardingNumber)

