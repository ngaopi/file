f=open("ing.txt","r")
x=f.read()
y=x.split()
i=0
count=0
while i<len(y):
    if "ing" in y[i]:
        count+=1
    i=i+1
print(count)


