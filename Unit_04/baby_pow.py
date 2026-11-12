#!/usr/local/bin/python3
import hashlib
import random
import string
import os

def proof_of_work():
    hash_funcs = {
        "sha256": hashlib.sha256,
        "md5": hashlib.md5,
        "keccak": hashlib.sha3_256
    }
    
    chosen_hash = random.choice(list(hash_funcs.keys()))
    s = "".join(random.sample(string.ascii_letters + string.digits, 20))
    prefix_len = random.randint(1, 4)
    prefix = s[:prefix_len]
    print(f"{chosen_hash}(xxxx + {s[prefix_len:]}) == {hash_funcs[chosen_hash](s.encode()).hexdigest()}")
    print("Mine xxxx:")
    ans = input().strip()
    return len(ans) == prefix_len and ans == prefix


if __name__ == "__main__":
    for _ in range(15):
        if not proof_of_work():
            exit()
    
    print("Congratulations miner! Here is your proof of solving the baby PoW task:")
    print(os.environ["PROOF_OF_WORK"])

    exit()