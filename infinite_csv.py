import bluetooth

bd_addr = "DC:A6:32:DE:78:1C"

port = 1

import numpy as np
import pandas as pd
import time
import sched
import sys


def remove_extra_headers(df, first_column):
    '''if row of headers is included multiple times throughout the csv file,
    remove these rows
    first_column: name of the header in the first column'''
    df = df.sort_values(first_column, 0)
    df = df.reindex(index=df.index[::-1])
   
    for i, j in enumerate(df['Time']):
        if j == 'Time':
            df = df[1:]
        else:
            break
    return df.reindex(index=df.index[::-1])
 

s = sched.scheduler(time.time, time.sleep)
def print_a_csv(filepath):
   
    df = pd.read_csv(filepath)
    df = remove_extra_headers(df, 'Time')
    s.enter(10, 1, print_a_csv, (filepath,))
    print(type(df['ECG_HR']))
 

# s.enter(10, 1, print_a_csv, ('nowave-clean.csv',))
# s.run()
 

df = pd.read_csv('nowave-clean.csv')
df = remove_extra_headers(df, 'Time')

#while True:
for wellnamedvariable in range(0,2):    
    for i in df.values:
        #print(i)

#         sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
#         sock.connect((bd_addr, port))
        #data = np.array2string(i)
        data = ','.join(i)
        #data = i.tostring()
#         for j in i:
#             data = data + j
            #print(j)
#             if j == '-':
#                 pass
#             else:
        #sock.send(data)
        sys.stdout.write(data)
        print(data)
        #print(data)
        #sock.send("\n")
        #sock.close()
        time.sleep(5)
        
        sys.stdout.flush()
        
        