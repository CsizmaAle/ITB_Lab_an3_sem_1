from pwn import *

#202.61.227.83:31337
host='202.61.227.83'
port='31338'
conn = remote(host, port)