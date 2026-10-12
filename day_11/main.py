from student import Student

def main():
    name=input("请输入学生姓名:")
    while True:
    
        score=input("请输入学生成绩:")
        try:
            score=int(score)
        except ValueError:
            print("输入错误，成绩必须是数字")
            continue
        try:
            student1=Student(name,score)
            print("学生创建成功")
            break
        except ValueError as e:
            print("学生创建失败:",e)
    student1.show_info()


if __name__ == "__main__":
    main()