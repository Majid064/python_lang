from typing import Union

per : Union[float,int] = 88
grade : Union[str,None] = None

if per >= 80:
    grade = "A+"
elif per >=70:
    grade = "A"
elif per >= 60:
    grade = "B"
elif per >= 50:
    grade = "C"
elif per >= 40:
    grade= "D"
elif per >=30:
    grade = "E"
else:
    grade = "Fail"

print(f"Dear student your percentage is {per} and you calculated grade is:\t {grade}")

