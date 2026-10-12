
#TASK 3 - UNIT 1
#Task no. 3 is hosted on the https://cryptohack.org platform.
#Create an account and solve the challenge called Public Keys ( https://cryptohack.org/challenges/rsa/ ).
#Please submit your potential solution/result on the platform to ensure it is correct.

e=65537
p=17 
q=23

N=p*q
plaintext=12

cipher=pow(12,e,N)

print(cipher)

#Rasp: 301 
