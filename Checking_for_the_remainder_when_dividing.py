def checking_for_the_remainder_when_dividing():
 import math
 print("Проверка на остаток при делении ")
 print("введите числa:")
 Number1 = int(input())
 Number2 = int(input())
 if(Number1%Number2==0)and(Number1!=0):
    print("Первое число делистся на второе без остатка и их частное равняется=", Number1/Number2)
 else:
    print("Первое число не делистся на второе без остатка и их произведение равняется=", Number1*Number2)
