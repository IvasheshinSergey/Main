def min_three_num():
 print("Выведение минимума из трех введенных чисел")
 print("введите три числа")
 Number1 = int(input())
 Number2 = int(input())
 Number3 = int(input())
 if (Number1<Number2)and(Number1<Number3):
    print("Минимальное число:", Number1)
 elif(Number2<Number1)and(Number2<Number3):
    print("Минимальное число:", Number2)
 elif(Number3<Number1)and(Number3<Number2):
    print("Минимальное число:", Number3)
