import math
a = int(input("온도를 입력하시오"))
b = input("화씨입니까 섭씨입니까?\n화씨:f 섭씨 c")
c=0
d=0

if b == "f":
    c = (5/9)*(a-32)
    print("회씨",a,"도 의값은 섭씨",c,"도입니다")
elif b == "c":
    c = (9/5)*a+32
    print("섭씨",a,"도 의값은 화씨",c,"도입니다")
else:
    print("f 또는 c를 입력하시오.")