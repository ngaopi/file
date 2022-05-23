# f=open("ring.jpg","rb")
# x=f.read()
# print(x)

# f=open("ring.jpg","rb")
# f1=open("my pic.jpg","wb")
# for pic in f:
#     f1.write(pic)

f=open("ring.jpg","rb")
x=f.seek(0,2)
# print(f.tell())
f1=(x,'bytes')
for pic in f1:
    print(pic)

