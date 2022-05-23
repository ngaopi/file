f=open("vowels_conso.txt","r")
x=f.read()
y=x.split()
i=0
while i<len(y):
    if y[i]=="a" or y[i]=="e"or y[i]=="i"or y[i]=="o"or y[i]=="u":
        print(y[i],"=","vowels")
    else:
        print(y[i],"=","consonant")
    i=i+1