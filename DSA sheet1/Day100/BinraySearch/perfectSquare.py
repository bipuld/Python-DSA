'''
Check Perfect Square or Not given Condition 
like 64 
You have been given an integer ‘N’. You are supposed to find if the given integer ‘N’ is a perfect square or not. A perfect square is an integer that is the square of an integer.


'''

def is_perfect(item):
    for i in range(1,item):
        if item==i*i:
            return item
    return -1
        
value=121
if is_perfect(value) != -1:
    print("{} is a perfect square".format(value))
else:
    print("{} is not a perfect square".format(value))
