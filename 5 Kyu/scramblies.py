# Complete the function scramble(str1, str2) that returns true if a portion of str1 characters 
# can be rearranged to match str2, otherwise returns false.

# Notes:

# Only lower case letters will be used (a-z). No punctuation or digits will be included.
# Performance needs to be considered.
# Examples

# scramble('rkqodlw', 'world') ==> True

# def scramble(s1, s2):
#     for i in s2:
#         if s1.count(i) >= 1:
#             continue
#         else:
#             return False
    
#     return True

# def scramble(s1, s2):
#     s2_list= [i for i in s2]
#     for i in s2:
#         if i in s1:
#             s2_list.remove(i)
    
#     if len(s2_list) == 0:
#         return True
#     return False

from collections import Counter

def scramble(s1, s2):
    counter1 = Counter(s1)
    counter2 = Counter(s2)

    for char, freq in counter2.items():
        if counter1[char] < freq:
            return False
    
    return True

# from collections import Counter
# def scramble(s1,s2):
#     # Counter basically creates a dictionary of counts and letters
#     # Using set subtraction, we know that if anything is left over,
#     # something exists in s2 that doesn't exist in s1
#     return len(Counter(s2)- Counter(s1)) == 0

# Taken from Codewars Solutions by 00kevn


print(scramble('rkqodlw', 'world'))