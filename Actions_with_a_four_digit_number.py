def actions_with_a_four_digit_number():
 import math
 print("Действия с четырехзначным числом")
 print("введите число")
 Number = int(input())
 x = [int(a) for a in str(Number)]
 if(Number%3==0):
    print("Число делится на 3 и сумма его чисел равняется=", sum(x))
 elif(Number%3!=0):
    print("Число не делится на 3 и произведение его чисел равняется=", math.prod(x))
