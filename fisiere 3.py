with open('globulete.txt','r') as f:
    a=f.readline()
r=int(a)+3
b=int(a)+r-2
with open('brad.txt','w') as f:
    f.write(str(int(a)+r+b))