import math
from random import randint
n1 = randint(1,9)
n2 = randint(1,9)
print(n1,"*",n2)
n3 = int(input(""))
n4 = n1*n2
if ( n3 == n4 ) :
    print(n3,"정답입니다")
else:
    print(n3,"정답이 아닙니다.")