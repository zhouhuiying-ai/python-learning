class Student:
    def __init__(self,name,age,score):
        # print("self是: ",self)
        self.name=name
        self.age=age
        self.score=score

    def introduce(self):
        print("我叫",self.name)
        print("我今年",self.age)
        print("我的成绩是",self.score)
        print("我的等级是",self.get_level())

    def is_pass(self):
        if self.score>=60:
            return True
        else:
            return False
        
    def get_level(self):
        if self.score>=90:
           return "优秀"
        elif self.score>=80:
           return "良好"
        elif self.score>=60:
           return "及格"
        else:
           return "不及格"   

student1=Student("小明",18,85)
# student2=Student("小红",19,92)

# print("student1是:",student1)
student1.introduce()
# student2.introduce()
# print(student1.is_pass())
# print(student2.is_pass())
# print(student1.get_level())
# print(student2.get_level())
# student1=Student()
# student1.name="小明"
# student1.age=18
# student1.score=85
print("是否及格:",student1.is_pass())
# student2=Student()
# student2.name="小红"
# student2.age=19
# student2.score=92

# print(student1.name)
# print(student1.age)
# print(student1.score)

# print(student2.name)
# print(student2.age)
# print(student2.score)
