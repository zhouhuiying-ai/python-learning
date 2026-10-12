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