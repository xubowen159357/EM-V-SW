light=1
under_lian=4
shard=5
underdif=7
cant_see=8
diffent=0
w=30
r=31
g=32
y=33
b=34
p=35
gb=36
black=37
def colormode(text,color=30,mode=0):
    return f'\033[{mode};{color}m{text}\033[0m'