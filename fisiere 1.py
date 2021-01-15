with open ('numere.txt','r') as f:
    a=f.readline()
    b=f.readline()
if int(a)> int(b):
    c=int(b)
if int(a)<int(b):
    c=int(a)
with open('minim.txt','w') as f:
    f.write(str(c))