f=open("lower_upper.txt","r")
x=f.read()
print(x)
i=0
count=0
count1=0
while i<len(x):
    if x[i].isupper():
        count+=1
    elif x[i].islower():
        count1+=1
    i=i+1
print("upper_case =",count)
print("lower_case =",count1)