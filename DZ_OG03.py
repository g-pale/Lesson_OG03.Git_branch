def square(side):
    'Функция выводит, периметр и площадь квадрата.'
    perimetr = side * 4
    square = side ** 2
    return f'Периметр квадрата - {perimetr},\nПлощадь квадрата - {square}'

result = square(5)
print(result)