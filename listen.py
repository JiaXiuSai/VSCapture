import serial
ser = serial.Serial(
		port='/dev/ttyUSB0',
		baudrate=19200,
		bytesize=serial.EIGHTBITS
		)
arr = []
while 1:
	arr.append(ser.read(1))
#	x = ' '.join(map(str, arr))
#	print(r'newone!\n')
#	print(x)
	print(arr)
