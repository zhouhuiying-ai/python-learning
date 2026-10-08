try:
    number=int(input("请输入一个数字:"))
    result=100/number

except ValueError:
    print("输入的不是数字")

except ZeroDivisionError:
    print("数字不能为0")
else:
        print(result)
finally:
     print("程序执行结束")
     