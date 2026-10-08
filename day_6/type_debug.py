try:
    age=int(input("请输入年龄： "))
  
except ValueError:
    print("输入错误：年龄必须是数字")
else:
        print("age=",age)
        print("type=",type(age))
  
