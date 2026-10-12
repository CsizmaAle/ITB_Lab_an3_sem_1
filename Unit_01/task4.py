#TASK 4 - UNIT 1

#Task no. 4 is hosted on the https://cryptohack.org platform.
#Use the same account to solve the challenge called Private Keys ( https://cryptohack.org/challenges/rsa/ ).
#lease submit your potential solution/result on the platform to ensure it is correct.

e = 65537
p = 857504083339712752489993810777
q = 1029224947942998075080348647219

if __name__ == "__main__":
    n=p*q
    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)
    print(d)
    
#121832886702415731577073962957377780195510499965398469843281