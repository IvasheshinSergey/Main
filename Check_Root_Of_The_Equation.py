def check_Root_Of_The_Equation():
 print("Определение наличия корней у уравнения")
 print("введите три числа")
 a = int(input())
 b = int(input())
 c = int(input())
 Discriminant =int( (b*b)-(4*a*c))
 if (Discriminant == 0)or(Discriminant >0):
    print("Да")
 elif(Discriminant<0):
    print("Нет")
