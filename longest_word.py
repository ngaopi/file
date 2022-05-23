f=open("longest_word.txt","r")
u=f.read().split()
print(u)
i=0
max=u[i]
while i<len(u):
    if len(u[i])>len(max):
        max=u[i]
    i=i+1
print(max)
f.close()

# f=open("longest_word.txt","r")
# u=f.read().split()
# i=0
# min=u[i]
# while i<len(u):
#     if len(u[i])<len(min):
#         min=u[i]
#     i=i+1
# print(min)
# f.close()

# user=input("enter the file name:")
# f=open(user,"r")
# u=f.read().split("\n")
# k=u
# i=0
# while i<len(k):
#     i=i+1
# print(i)
# f.close()
