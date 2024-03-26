"""
You are given a string 'STR'. The string contains [a-z] [A-Z] [0-9] [special characters]. You have to find the reverse of the string.
For example:
 If the given string is: STR = "abcde". You have to print the string "edcba".
follow up:
Try to solve the problem in O(1) space complexity.
"""


def string_swap(st, start=0, end=None):
    if end is None:
        end = len(st) - 1

    if start > end:
        return st

    st = list(st)


    st[start], st[end] = st[end], st[start]
    print(st)
    st = "".join(st)
    print(st)

    return string_swap(st, start + 1, end - 1)


original_string = "abcde"
print(string_swap(original_string))
