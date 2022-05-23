# take user inputs for file name and from any file bring out number of words
# letters and line.
# user=input("enter the file name:")
# f=open(user,"w+")
# f.write("good morning?\nhave a nice day ")
# x=f.seek(0,0)
# d=f.readlines()
# a=0
# while a<len(d):
#     a+=1
# x=f.seek(0,0)
# b=f.read()
# i=0
# count=0
# while i<len(b)-1:
#     k=b[i]+b[i+1]
#     count+=1
#     i=i+1
# l=b.split()
# i=0
# count1=0
# while i<len(l)-1:
#     m=l[i]+l[i+1]
#     count1+=1
#     i=i+1
# print(a,"\n",count,count1)

user=input("enter the file name:")
f=open(user,"r")
lines=0
words=0
char=0
for i in(f):
    words_list=i.split("\n")
    lines+=1
    words=words+len(words_list)
    char+=len(i)
print("line:",lines,"words:",words,"char:",char)

# print(words_list)