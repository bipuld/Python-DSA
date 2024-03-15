"""
You are given a positive integer ‘n’.
Your task is to find and return its square root. If ‘n’ is not a perfect square, then return the floor value of sqrt(n).
Example:
Input: ‘n’ = 7

Output: 2

Explanation:
The square root of the number 7 lies between 2 and 3, so the floor value is 2.
"""


# Using Binary Search
def square_root(n):
    l = 1
    r = n
    res = 0
    while l <= r:
        mid = (l + r) // 2
        if mid * mid == 2:
            return mid
        elif (mid * mid) > n:
            r = mid - 1
        else:
            l = mid + 1
            res = mid
    return res


numbers = int(input("Enter the number :"))
ans = square_root(numbers)
print("Answer is ", ans)
