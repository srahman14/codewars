# n=7, k=3 => means 7 people in a circle
# one every 3 is eliminated until one remains
# [1,2,3,4,5,6,7] - initial sequence
# [1,2,4,5,6,7] => 3 is counted out
# [1,2,4,5,7] => 6 is counted out
# [1,4,5,7] => 2 is counted out
# [1,4,5] => 7 is counted out
# [1,4] => 5 is counted out
# [4] => 1 counted out, 4 is the last element - the survivor!

# In this kata you have to correctly
# return who is the "survivor", ie: the last element of a Josephus permutation.

# basically I have to iterate through a list 
# every elemnt that lands after 3 counts is popped
# if it reaches the end of the list it starts from the beginning

# def josephus_survivor(n,k):
#     josephusCircle = list(range(1, n + 1))
#     count = 0
#     k -= 1
#     while len(josephusCircle) > 1:
#         # do this
#         start = 0
#         currPos = josephusCircle[start]

#         execute = josephusCircle[:k]
#         josephusCircle.pop(execute)


# print(josephus_survivor(7, 0)) 

x = [1,2,3]
x.remove(3)
print(x)