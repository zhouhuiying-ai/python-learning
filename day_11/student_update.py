class Student:
    def __init__(self,name,score):
        self.name=name
        if self.is_valid_score(score):
            self.score=score
        else:
            raise ValueError("成绩必须在0到100之间")

    def is_valid_score(self,score):
        return 0<=score<=100

    def get_level(self):
        if self.score>=90:
            return "优秀"
        elif self.score>=80:
            return "良好"
        elif self.score>=60:
            return "及格"
        else:
            return "不及格"
        

    def update_score(self,new_score):
        if not self.is_valid_score(new_score):
            raise ValueError("成绩必须在0到100之间")
        self.score=new_score
    def show_info(self):
        print("姓名:",self.name)
        print("成绩:",self.score)
        print("等级:",self.get_level())



# # student1=Student("小明",150)
# # print("修改前的成绩:",student1.score)
# # student1.update_score(95)
# # print("修改后的成绩:",student1.score)
# student1=Student("小明",85)
# try:
#     student1.update_score(150)
#     print("学生修改成功")
# except ValueError as e:
#     print("学生修改失败:",e)
# print("当前成绩:",student1.score)
# print("程序继续运行")
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
