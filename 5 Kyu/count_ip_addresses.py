# Implement a function that receives two IPv4 addresses, and returns the number of addresses between them 
# (including the first one, excluding the last one).

# All inputs will be valid IPv4 addresses in the form of strings. 
# The last address will always be greater than the first one.

def ips_between(start, end):
    # TODO
    startList = start.split('.')
    endList = end.split('.')

    startTotal = 0
    endTotal = 0

    exponent = 3
    # for i in startList:
    #     if i == 0:
    #         exponent -= 1
    #         continue
    #     startTotal += int(i) * (256**exponent)
    #     exponent -= 1
    
    # exponent = 3
    # for i in endList:
    #     if i == 0:
    #         exponent -= 1
    #         continue

    #     endTotal += int(i) * (256**exponent)
    #     exponent -= 1

    currExp = 3
    total = 0
    for i in range(4):
        if (startList[i]) == (endList[i]):
            currExp -= 1
            continue 
        else:
            total += (int(endList[i]) * 256**currExp) - (int(startList[i])* 256**currExp)

    return total

    # newList = []
    # for i in range(4):
    #     newList.append(int(startList[i]) ** exponent)

    
    # return newList

print(ips_between("10.0.0.0", "10.0.0.50"))
