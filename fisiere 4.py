with open('input.txt','r') as f:
    n=f.readline()
a=int(n)-2
b=int(n)-1
c=int(n)+1
d=int(n)+2
with open('output.txt','w') as f:
    f.write(str(a)+" "+str(b)+" "+n+" "+str(c)+" "+str(d))
