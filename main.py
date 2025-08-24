def square(side):
    'Функция выводит, периметр и площадь квадрата.'
    perimetr = side * 4
    square = side ** 2
    diagonal = (side ** 2 + side ** 2)**0.5
    return f'Периметр квадрата - {perimetr},\nПлощадь квадрата - {square}'

<<<<<<< Updated upstream

def area_circle(r):
    s = math.pi * r**2
    return s

def area_square(a):
    S_s = a**2
    return S_s
=======
result = square(5)
print(result)
>>>>>>> Stashed changes
