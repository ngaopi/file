# f=open("message.txt","r")
# content=f.read(6)
# print(content)
# more_content=f.read(12)
# print(more_content)
# f.close()

# try:
#     f=open("message.txt","r")
#     content=f.read(6)
#     print(content)
#     more_content=f.read(12)
#     print(more_content)
# finally:
#     f.close()

# with open("message.txt","r") as f:
#     content=f.read(6)
#     print(content)
#     more_content=f.read(12)
#     print(more_content)
    
# with open("python.txt","w")as f:
#     f.write("python is awsome")
#     f.write("i love python")

with open("python.txt","a")as f:
    f.write("\npython is my favourite programming language")
    
# with open("python.txt","r")as f:
#     lines=f.read()
#     print(lines)
    