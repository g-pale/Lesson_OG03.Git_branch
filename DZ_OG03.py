def square(side):
    'Функция выводит, периметр, площадь и длину диагонали квадрата.'
    perimetr = side * 4
    square = side ** 2
    diagonal = (side ** 2 + side ** 2)**0.5
    return f'Периметр квадрата - {perimetr},\nПлощадь квадрата - {square},\nДиагональ квадрата - {diagonal}'

result = square(5)
print(result)