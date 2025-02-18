# Complete the function that

# accepts two integer arrays of equal length
# compares the value each member in one array to the corresponding member in the other
# squares the absolute value difference between those two values
# and returns the average of those squared absolute value difference between each member pair.

# [1, 2, 3], [4, 5, 6]              -->   9   because (9 + 9 + 9) / 3
# [10, 20, 10, 2], [10, 25, 5, -2]  -->  16.5 because (0 + 25 + 25 + 16) / 4
# [-1, 0], [0, -1]                  -->   1   because (1 + 1) / 2

def solution(array_a, array_b):
    if len(array_a) == 0 and len(array_b) == 0: return 0
    numItems = len(array_a) 

    start = 0
    l = []
    while len(array_a) > 0 and len(array_b) > 0:
        if start == numItems:
            break
        diff = array_a[start] - array_b[start]
        if diff < 0:
            l.append((diff*-1)**2)
        else:
            l.append(diff**2)
        
        start += 1
    
    return sum(l)/numItems

print(solution([1,2,3], [4,5,6]))
print(solution([10, 20, 10, 2], [10, 25, 5, -2]))
print(solution([-1, 0], [0, -1]))