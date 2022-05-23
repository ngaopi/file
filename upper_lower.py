f=open("upper_lower.txt","r")
x=f.read()
i=0
while i<len(x):
    if x[i]==x[i][0]:
        b=x[i][0].upper()
    i=i+1
    print(b,end=" ")
f.close()

