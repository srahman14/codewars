# Starting with "1" the following lines are produced by 
# "saying what you see", so that line two is "one one", 
# line three is "two one(s)", line four is "one two one one".

# Write a function that given a starting value as a string, 
# returns the appropriate sequence as a list. 
# The starting value can have any number of digits. 
# The termination condition is a defined by the maximum 
# number of iterations, also supplied as an argument.

# Example
#      1
#      11
#      21
#     1211
#    111221
#    312211
#   13112221
#  1113213211
#       .
#       .
#       .

# When there is one consequential one -> 1 = 11 
# When there is two consequential ones -> 11 = 21
# This is just RLE

def look_and_say(data='1', maxlen=5):
    seq = [data]
    curr = ""
    while len(seq) < maxlen:
        curr = seq[len(seq)-1]

        count = 0
        curr_num = ""
        next_seq = ""
        for i in curr:
            curr_num = i
            if i != curr_num:
                next_seq = f"{str(count)}{curr_num}"
                curr_num = i
            else:
                count+=1
        seq.append(next_seq)
    
    return seq

print(look_and_say('1', 10))

