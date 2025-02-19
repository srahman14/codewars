# def move_zeros(lst):
#     for i in lst:
#         if i == 0:
#             lst.remove(i)
#             lst.append(i)
    
#     return lst

# def move_zeros(lst):
#     zeroes = len(lst)
#     lst = [i for i in lst if i != 0]
#     zeroes -= len(lst)
#     for i in range(zeroes):
#         lst.append(0)
    
#       return lst


def move_zeros(lst):
    return [i for i in lst if i != 0] + [0] * lst.count(0)

lst1 = [1, 0, 1, 2, 0, 1, 3]

print(move_zeros(lst1))

