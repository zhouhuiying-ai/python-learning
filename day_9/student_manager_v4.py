def main():
    students=load_students()
    while True:
        print("1.添加学生")   
        print("2.查看所有学生")
        print("3.退出")

        choice= input("请输入菜单选项:")
        if choice=="1":
             add_student(students)
        elif  choice=="2":
            view_all_students(students)
        elif choice=="3":
            break
        else:
            print("菜单选项错误，请输入1、2或3")

def add_student(students):
    name=input("请输入姓名:")
    try:
        score=int(input("请输入成绩:"))
    except ValueError:
        print("成绩必须是数字")
        return
    if score>=0 and score<=100:
        student={
            "name":name,
            "score":score
        }
        students.append(student)
        save_student(student)
        
    else:
        print("成绩必须在0到100之间")

        
def view_all_students(students):
    if students==[]:
        print("当前没有学生")
        return
    else:
        for student in students:
            name=student["name"]
            score=student["score"]
            result=check_pass(score)
            print("姓名:",name)
            print("成绩:",score)
            print("结果:",result)
def check_pass(score):
    if score>=60:
        return "及格"
    else:
        return "不及格"
    
def save_student(student):
    name=student["name"]
    score=student["score"]
    with open("students.txt","a")as f:
        f.write(name+","+str(score)+"\n")

def load_students():
    students=[]
    try:
        with open("students.txt","r") as f:
            lines=f.readlines()    
        for line in lines:
            try:
                line=line.strip()
                parts=line.split(",")
                if len(parts)!=2:
                    print("文件格式错误")
                    continue
                name=parts[0]
                score=int(parts[1])
                if 0<=score<=100:   
                    student={
                        "name":name,
                        "score":score
                    }
                    students.append(student)
                else:
                    print("文件中的成绩范围错误")
                    continue
            except (ValueError, IndexError):
                print("文件格式错误")
        return students
    except FileNotFoundError:
        print("文件不存在")
        return students
        
main()
