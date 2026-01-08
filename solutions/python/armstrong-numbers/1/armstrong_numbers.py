def is_armstrong_number(number):
    digits = str(number)
    length = len(digits)
    sum_of_powers = sum(int(digit) ** length for digit in digits)
    return number == sum_of_powers
