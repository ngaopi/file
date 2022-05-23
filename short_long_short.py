

f=open("short_long.txt","r")
x=f.read()
y=x.split()
i=0
while i<len(y)-1:
    d=y[i+1]+y[i]+y[i+1]
    i=i+1
print(d)
