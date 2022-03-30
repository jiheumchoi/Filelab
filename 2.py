import math
a = int(input("정수를 입력하시오"))
result=0
for i in range(0,a+1):
    if i%2==0 :
        result=result+i
print(result)