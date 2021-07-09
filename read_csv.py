import sys
import bluetooth
#from subprocess import Popen, PIPE
import subprocess
import os
import binascii

os.system('sudo hciconfig hci0 down')
os.system('sudo hciconfig hci0 up')
os.system('sudo hciconfig hci0 leadv 3')


bd_addr = "DC:A6:32:DE:78:1C"

port = 1

for line in sys.stdin:
    print('--- read csv---')
    line = line.split(',')     
    dataurl = binascii.hexlify(line[0].encode())
    iterable = iter(dataurl.decode())
    dataurl = ' '.join(a+b for a, b in zip(iterable,iterable))
    os.system(f'sudo hcitool -i hci0 cmd 0x08 0x0008 19 02 01 06 03 03 aa fe 11 16 aa fe 10 00 03 {dataurl}')
