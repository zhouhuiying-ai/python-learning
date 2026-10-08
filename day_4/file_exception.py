try:
    with open("result.txt","r") as file:
        content=file.read()

except FileNotFoundError:
    print("文件不存在")

else:
    print(content)
finally:
    print("程序执行结束")
