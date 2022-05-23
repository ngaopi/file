# banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
# f=open("banks_list.txt","w")
# for name in banks_list:
#     f.write(name)
#     f.write("\n")
# f.close()

f=open("file_reverse.txt","r")
x=f.read()
y=x.split()
i=0
b=[]
while i<len(y):
    b.append(y[-i-1])
    i=i+1
print(b)





