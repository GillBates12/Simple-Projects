#Letter Grade Bot

pointsPossible = 100
studentName = input("What is the name of the student?: ")
try:
    score = int(input("Student Score: "))
except Exception:
    print("Please enter a valid number")
percent = score / pointsPossible
grade = "ERROR"


if 1 >= percent >= 0.9:
    grade = "A"
elif 0.9 > percent >= 0.8:
    grade = "B"
elif 0.8 > percent >= 0.7:
    grade = "C"
elif 0.7 > percent >= 0.6:
    grade = "D"
else:
    grade = "FAIL"

print("{} - {}".format(studentName, grade))


