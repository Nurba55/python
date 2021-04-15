def calc():
    a = float(input('Введите первое число :'))
    b = float(input('Введите второе число : '))
    c = input('Какую операцию совершить: +  -  *  / ')
    if c == '+':
        print(a+b)
    elif c == '-':
        print(a-b)
    elif c == '/':
        print(a/b)
    elif c == '*':
        print(a*b)
    else:
        print('Не правильный ввод')


calc()
