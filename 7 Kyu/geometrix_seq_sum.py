# A geometric progression / series is the sum of a geometric sequence.

# A geometric sequence is a sequence of numbers that scale by a common ratio, usually denoted as r. To get the next term, multiply the current term by this value. The first term is provided for this kata.

# For example, the first 4 terms of the geometric sequence with first term 2 and ratio 3 is 2, 6, 18, 54. Notice that, given any term, it is 3 times larger than the last term for this case.

# A geometric series is just the first n terms of the sequence summed together. For instance, the sum of the first four terms of the example provided above is 
# 2
# +
# 6
# +
# 18
# +
# 54
# =
# 80
# 2+6+18+54=80.

# Kata Task

# Complete the function which will help you compute a geometric progression / series.

# The parameters provided are as follows:

# a is the first term
# r is the common ratio
# n is the amount of terms
# Example:

# a = 2, r = 3, n = 5 should return 242.

# Input constraints:

# a: 1 - 10
# r: -10 - 10
# n: 2 - 15
# Tests:

# 5 fixed tests
# 50 random tests
# For tests with decimal values your solution must have precision of 1e-9.

# More info: https://en.wikipedia.org/wiki/Geometric_progression

def geometric_sequence_sum(a, r, n):
    sum = 0 
    for i in range(1, n):
        sum += (a * (r ** (i)))
    
    return sum + a 

print(geometric_sequence_sum(2, 3, 5))