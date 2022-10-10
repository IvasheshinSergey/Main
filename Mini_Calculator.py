def mini_Calculator():
     import math
     print("Мини калькулятор")
     print("введите число1:")
     Number1 = int(input())
     print("введите число2:")
     Number2 = int(input())
     print("введите знак:")
     sign = str(input())
     if(sign=='+'):
        print(Number1+Number2)
     elif(sign=='-'):
        print(Number1-Number2)
     elif(sign=='*'):
        print(Number1*Number2)
     elif(sign=='/'):
        print(Number1/Number2)
