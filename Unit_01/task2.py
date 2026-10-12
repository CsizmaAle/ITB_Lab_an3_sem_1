
#TASK 2 - UNIT 1
#Task no. 2 requires you to break the hash of a secret password.
#The hash is: 8ec47631827329eb114714a20d9b3eeb8a9a4293bd5d6823af0632e8d4f30dfa 
#Note: the secret password is part of the famous rockyou.txt dictionary.


import hashlib
import sys
import zipfile

ZIP_FILE = "rockyou.txt.zip"
target="8ec47631827329eb114714a20d9b3eeb8a9a4293bd5d6823af0632e8d4f30dfa"


def crack_bytes(target_hash, raw):
    for lineno, line in enumerate(raw.splitlines(), 1):
        word = line.strip()
        if not word:
            continue
        digest = hashlib.sha256(word).hexdigest()
        if digest == target_hash:
            return word.decode("latin-1"), lineno
    return None, None


def main():
    print(f"[*] Hash tinta : {target}\n")

    with zipfile.ZipFile(ZIP_FILE) as z:
        rockyou = z.namelist()[0]
        print(f"[*] Caut in : {rockyou}")
        password, lineno = crack_bytes(target, z.read(rockyou))
        if password is not None:
            print(f"\n[+] GASIT! Parola este: {password}")
            print(f"    Sursa: {rockyou} (linia {lineno})")
            return

    print("\n[-] Parola nu a fost gasita.")


if __name__ == "__main__":
    main()


#[+] GASIT! Parola este: chainybaby*2791
# Sursa: rockyou.txt (linia 9199992)