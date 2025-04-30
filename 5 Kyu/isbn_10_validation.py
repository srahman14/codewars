# ISBN-10 identifiers are ten digits long. 
# The first nine characters are digits 0-9. 
# The last digit can be 0-9 or X, to indicate a value of 10.

# An ISBN-10 number is valid if the sum of the digits 
# multiplied by their position modulo 11 equals zero.

# Example
# ISBN     : 1 1 1 2 2 2 3 3 3  9
# position : 1 2 3 4 5 6 7 8 9 10
# (1*1 + 1*2 + 1*3 + 2*4 + 2*5 + 2*6 + 3*7 + 3*8 + 3*9 + 9*10) % 11 = 0

def valid_ISBN10(isbn): 
    if len(isbn) < 10 or len(isbn) > 10:
        return False
    dct = {}
    for i, x in enumerate(isbn):
        dct[i+1] = x

    total = 0 
    for i in dct:
        if i < 9 and not dct[i].isdigit():
            return False
        if dct[i].isdigit():
            total += (int(i) * int(dct[i]))
        elif dct[i] == 'X':
            total += (i * 10)

    if total % 11 == 0:
        return True


# valid_ISBN10('1112223339')
# print(valid_ISBN10('123456789T'))
# print(valid_ISBN10('XXXXXXXXXX'))
print(valid_ISBN10('1234'))