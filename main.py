import Min_three_num
import Check_Root_Of_The_Equation
import Actions_with_a_four_digit_number
import Definition_of_a_three_digit_number
import Checking_for_the_remainder_when_dividing
import Mini_Calculator

MenuMin_three_num = '1'
MenuCheck_Root_Of_The_Equation = '2'
MenuActions_with_a_four-digit_number = '3'
MenuDefinition_of_a_three-digit_number = '4'
MenuChecking_for_the_remainder_when_dividing = '5'
MenuMini_Calculator = '6'

print(
'''
Меню:
1. Выведение минимума из трех введенных чисел
2. Определение наличия корней у уравнения
3. Действия с четырехзначным числом
4. Определение трехзначного числа
5. Проверка на остаток при делении 
6. Мини калькулятор
(Наберите номер пункта и нажмите <ENTER>)
'''
)

menu_value = input()
if      menu_value == MenuMin_three_num:
    Min_three_num.min_three_num()
elif    menu_value == MenuCheck_Root_Of_The_Equation:
    Check_Root_Of_The_Equation.check_Root_Of_The_Equation()
elif    menu_value == MenuActions_with_a_four-digit_number:
    Actions_with_a_four_digit_number.actions_with_a_four_digit_number()
elif    menu_value == MenuDefinition_of_a_three-digit_number:
    Definition_of_a_three_digit_number.definition_of_a_three_digit_number()
elif    menu_value == MenuChecking_for_the_remainder_when_dividing:
    Checking_for_the_remainder_when_dividing.checking_for_the_remainder_when_dividing()
elif    menu_value == MenuMini_Calculator:
    Mini_Calculator.mini_Calculator()
else:    
    print("Неверные данные!")

input("Нажмите <ENTER> для выхода")
