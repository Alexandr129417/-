digit1 = int(input('Введіть перше число: '))

digit2 = int(input('Введіть друге число: '))

what_to_do = input("Що робимо? ('/', '*', '+', '-') : ")

if what_to_do == '/':
    if digit2 == 0:
        print("Помилка: Ділення на нуль!")
    else:
        print(digit1 / digit2)

elif what_to_do == '*':
    print(digit1 * digit2)

elif what_to_do == '+':
    print(digit1 + digit2)

elif what_to_do == '-':
    print(digit1 - digit2)

else:
    print("Невідома операція!")
