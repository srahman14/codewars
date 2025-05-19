# Determine whether a non-negative integer number is colorful or not.

# 263 is a colorful number because [2, 6, 3, 2*6, 6*3, 2*6*3] are all different; whereas
# 236 is not colorful, because [2, 3, 6, 2*3, 3*6, 2*3*6] has 6 twice.

# So take all consecutive subsets of digits, take their products, and ensure all the products are different.

# Examples
# 263  -->  true
# 236  -->  false

def colourful(num):
    nums = [int(i) for i in str(num)]
    print(nums)

colourful(253)

    