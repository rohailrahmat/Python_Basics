# schoool grading system 
score = 999
 
if score > 100:
    exit("You have give wrong input")


if score >= 90:
    grade = "A++"
elif score >= 80:
    grade ="A+"
elif score >= 70:
    grade = "A"
elif score >= 60:
    grade = "B"
elif score >= 50:
    grade = "C"
elif score >= 40:
    grade = "D"
elif score < 40 :
    grade = "Try Again Next Year"
else:
    print("Wrong input please check")

print(grade)
