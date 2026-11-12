#!/usr/local/bin/python3
import hashlib
import random
import os

def proof_of_work():
    hash_funcs = {
        "sha256": hashlib.sha256,
    }
    
    chosen_hash = random.choice(list(hash_funcs.keys()))
    prefix_len = 5
    s = "".join(random.sample("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmn0123456789", prefix_len))
    prefix = s[:prefix_len]
    print(f"{chosen_hash}(xxxx) == {hash_funcs[chosen_hash](s.encode()).hexdigest()}")
    print("Mine xxxx:")
    ans = input().strip()
    return len(ans) == prefix_len and ans == prefix


if __name__ == "__main__":
    for _ in range(5):
        if not proof_of_work():
            exit()
    
    print("Congratulations miner! Here is your proof of solving the adult PoW task:")
    print(os.environ["PROOF_OF_WORK"])

    exit()