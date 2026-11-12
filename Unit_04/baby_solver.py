import itertools
from pwn import *
import hashlib
import string


#202.61.227.83:31337
host='202.61.227.83'
port='31337'


#batman@Alexandras-MacBook-Air DCT_Fraancmasonerie % nc 202.61.227.83 31337
#keccak(xxxx + EaPL5Agw2O0FIudj) == ea771bfb279d4168cec71a018b6abc415f9d3828d946deae4d52b8b8ed1fab70
#Mine xxxx:


def find_xxxx(hash_func, hash_value, suffix):
    length=20-len(suffix)
    #for length in range(1, 5):  
    for candidate in map(''.join, itertools.product(string.ascii_letters + string.digits, repeat=length)):
        combined = candidate + suffix
        if hash_func(combined.encode()).hexdigest() == hash_value:
            return candidate
    return None


def get_hash_function(name):
    if name == "sha256":
        return hashlib.sha256
    elif name == "md5":
        return hashlib.md5
    elif name == "keccak":
        return hashlib.sha3_256
    else:
        raise ValueError(f"Unsupported hash function: {name}")
    

def preluare_hash_func(line):
    # preluare functie de hash
    hash_func=line.split('(')[0]
    hash_func=hash_func.strip()
    #print(hash_func)
    return get_hash_function(hash_func)

def preluare_hash(line):
    # preluare hash
    hash=line.split('==')[1]
    hash=hash.strip()
    #print(hash)
    return hash

def preluare_suffix(line):
    #preluare sufix
    suffix=line.split('+')[1]
    suffix=suffix.split(')')[0]
    suffix=suffix.strip()
    #print(suffix)
    return suffix


if __name__ =="__main__":
    conn = remote(host, port)
    
    for _ in range(15):
        line=conn.recvline().decode()
        print(line)
        print(conn.recvline().decode())
        xxxx = find_xxxx(preluare_hash_func(line), preluare_hash(line), preluare_suffix(line))
        conn.sendline(xxxx.encode())
        print(conn.recvline().decode())

    
    print(conn.recvall(timeout=2).decode(errors='ignore'))
    conn.close()

