def validate_triangle(sides):
    a, b, c = sides
    return 0 not in sides and (a + b >= c) and (b + c >= a) and (a + c >= b)

def equilateral(sides):
    a, b, c = sorted(sides)
    return validate_triangle(sides) and a == c


def isosceles(sides):
    a, b, c = sides
    return validate_triangle(sides) and (a == b or a == c or b == c)


def scalene(sides):
    a, b, c = sides
    return validate_triangle(sides) and (a != b and a != c and b != c)
