def show_welcome():
    print("学生成绩管理程序")

def input_student():
    name=input("请输入姓名： ")
    if name=="q":
        return None,None
    try:
        score=int(input("请输入成绩: "))
        return name,score
    except ValueError:
        print("成绩必须是数字")
        return None,None
    
def check_pass(score):
    if score>=60:
        return "及格"
    else:
        return "不及格"

def show_student(name,score,result):
    print("姓名: ",name)
    print("成绩: ",score)
    print("结果: ",result)

def main():
    students=[]

    show_welcome()

    while True:
        name,score=input_student()
        if name is None:
            break

        if score is None:
            return
        student={
            "name":name,
            "score":score
            }
  
        students.append(student)

    for student in students:
        name = student["name"]
        score = student["score"]
        result = check_pass(score)
        show_student(name, score, result)
    # result=check_pass(score)
    # show_student(name,score,result)

main()
