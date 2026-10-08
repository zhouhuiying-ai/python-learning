try:
    with open("result.txt","r") as file:
        content=file.read()
    print(content)
except FileNotFoundError:
    print("文件不存在")
print("程序继续执行")
