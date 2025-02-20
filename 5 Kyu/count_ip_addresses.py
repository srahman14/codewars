# Implement a function that receives two IPv4 addresses, and returns the number of addresses between them 
# (including the first one, excluding the last one).

# All inputs will be valid IPv4 addresses in the form of strings. 
# The last address will always be greater than the first one.

def ips_between(start, end):
    # TODO
    startList = start.split('.')
    endList = end.split('.')
    
    endTotal = 0
    startTotal = 0
    
    for i in range(4):
        startTotal = startTotal + (int(startList[i]) * 256**(3 - i))
        endTotal = endTotal + (int(endList[i]) * 256**(3 - i))

    return endTotal - startTotal


# from solution import ips_between
# import codewars_test as test

# @test.describe("Tests")
# def tests():

#     @test.it("Sample tests")
#     def fixed_tests():
#         test.assert_equals(ips_between("150.0.0.0", "150.0.0.1"), 1)
#         test.assert_equals(ips_between("10.0.0.0", "10.0.0.50"), 50)
#         test.assert_equals(ips_between("20.0.0.10", "20.0.1.0"), 246)
#         test.assert_equals(ips_between("10.11.12.13", "10.11.13.0"), 243)
#         test.assert_equals(ips_between("160.0.0.0", "160.0.1.0"), 256)