for i in a:
	try:
		string = string + (hex(ord(i.decode()))).replace('0x', '  ')
	except:
		string = string + ' ff'
