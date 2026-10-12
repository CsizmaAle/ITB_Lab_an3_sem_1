#TASK 7 - UNIT 1

#Task no. 7 is hosted on the https://cryptohack.org platform.
#Use the same account to solve the challenge called Point Negation ( https://cryptohack.org/challenges/ecc/ ).
#Please submit your potential solution/result on the platform to ensure it is correct.

#Y^2=X^3+497X+1768 mod 9739
# P+Q=O

P=(8045,6936)
O=(0,0)

# => Q=-P
# pt o curba eliptica opusul unui punct e oglinditul sau in raport cu axa OX
# Q=(8045, y)
# y= -6936 mod 9739

Q=(8045, pow(-6936,1,9739))
print(Q)


#Rasp: crypto{8045,2803}