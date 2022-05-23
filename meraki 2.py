f=open("meraki 2.txt","r")
x=f.readlines()
c=0
for i in x:
    c=c+1
print("count",c)
f.close()
