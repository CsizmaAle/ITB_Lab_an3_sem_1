#TASK 5 - UNIT 1

#Task no. 5 is hosted on the https://cryptohack.org platform.
#Use the same account to solve the challenge called RSA Decryption ( https://cryptohack.org/challenges/rsa/ ).
#Please submit your potential solution/result on the platform to ensure it is correct.


N = 882564595536224140639625987659416029426239230804614613279163
e = 65537
c = 77578995801157823671636298847186723593814843845525223303932
p=857504083339712752489993810777
q=1029224947942998075080348647219

# https://factordb.com/?query=882564595536224140639625987659416029426239230804614613279163&full=1

if __name__ == "__main__":
    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)
    m = pow(c, d, N)
    print(m)

# 13371337