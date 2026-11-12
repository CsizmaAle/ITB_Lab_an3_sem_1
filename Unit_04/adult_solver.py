import itertools
from pwn import *
import hashlib

#202.61.227.83:31338
host='202.61.227.83'
port='31338'

def find_xxxx(hash_value):
    length=5 
    contor=0
    for candidate in map(''.join, itertools.product("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmn0123456789", repeat=length)):
        contor+=1
        if contor%1000000==0:
            print("Contor: ", contor)
        if hashlib.sha256(candidate.encode()).hexdigest() == hash_value:
            return candidate
    return None


def preluare_hash(line):
    # preluare hash
    hash=line.split('==')[1]
    hash=hash.strip()
    #print(hash)
    return hash



if __name__ =="__main__":
    conn = remote(host, port)
    
    for _ in range(5):
        print("\n\n Round ", _+1)
        line=conn.recvline().decode()
        print(line)
        print(conn.recvline().decode())
        xxxx = find_xxxx(preluare_hash(line))
        conn.sendline(xxxx.encode())
        print(conn.recvline().decode())

    print(conn.recvall(timeout=2).decode(errors='ignore'))
    conn.close()