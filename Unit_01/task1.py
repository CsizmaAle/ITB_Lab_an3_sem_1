
#TASK 1 - UNIT 1
# Task no. 1 requires you to compute the following hash: sha256(<Your First Name>.<Your Last Name>.<SHA256("Blockchain")>)

import hashlib

text="Alexandra.Csizmadia." + str(hashlib.sha256("Blockchain".encode()).hexdigest())
print(hashlib.sha256(text.encode()).hexdigest())

#Rez: f86abe6bc0e653503ccb72e9385f50c3abed48b1ff791d3a35075d3f66a7352e