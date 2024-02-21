import random

a='qwertyuiopasdfghjklzxcvbnm1234567890'
b=[]
b+=a
a=b
b='QWERTYUIOPASDFGHJKLZXCVBNM1234567890'
c=[]
c+=b
b=c

def rand(Caps:bool):
    if Caps:c=b
    else:c=a
    uuid=''
    for i in range(8):
        uuid+=c[random.randint(0,len(c)-1)]
    uuid+='-'
    for i in range(4):
        uuid+=c[random.randint(0,len(c)-1)]
    uuid+='-'
    for i in range(4):
        uuid+=c[random.randint(0,len(c)-1)]
    uuid+='-'
    for i in range(4):
        uuid+=c[random.randint(0,len(c)-1)]
    uuid+='-'
    for i in range(12):
        uuid+=c[random.randint(0,len(c)-1)]
    return uuid

