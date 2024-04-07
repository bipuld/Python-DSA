"""Ninja is sitting in an examination hall. He is encountered with a problem statement, "Find ‘X’ to the power ‘N’ (i.e. ‘X’ ^ ‘N’). Where ‘X’ and ‘N’ are two integers."

Ninja was not prepared for this question at all, as this question was unexpected in the exam.

He is asking for your help to solve this problem. Help Ninja to find the answer to the problem.

Note :

For this question, you can assume that 0 raised to the power of 0 is 1."""


def power(x, n):
    if n == 0:
        return 1
    elif n >= 1:
        return x * power(x,n-1)
    else:
        return 1/power(x,-n)


print(power(2, 3))
