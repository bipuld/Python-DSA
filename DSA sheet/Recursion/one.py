"""You have been given an integer 'N'.
Your task is to return true if it is a power of two. Otherwise, return false.
An integer 'N' is a power of two, if it can be expressed as 2 ^ 'K' where 'K' is an integer.
For example:
'N' = 4,
4 can be represented as 2^2. So, 4 is the power of two, and hence true is our answer."""

def powerOfTwo(n):
    if n == 1:
        return True
    elif n % 2 == 0 and n > 0:
        return powerOfTwo(n//2)
    else:
        return False

print(powerOfTwo(88))