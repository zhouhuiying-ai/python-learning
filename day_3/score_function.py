def check_score(score):
    if score>=90:
        return "excellent"
    elif score>=60:
        return "pass"
    else:
        return "fail"
result=check_score(85)
print(result)
