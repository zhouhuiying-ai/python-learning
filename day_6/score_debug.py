try:
    score=int(input("请输入成绩： "))
except ValueError:
    print("成绩必须是数字")
else:
    if score>=60:
        print("及格")
    else:
        print("不及格")
