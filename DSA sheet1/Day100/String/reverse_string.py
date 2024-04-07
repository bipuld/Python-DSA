# You are given a string 'STR'. The string contains [a-z] [A-Z] [0-9] [special characters]. You have to find the reverse of the string.
#
# For example:
#
#  If the given string is: STR = "abcde". You have to print the string "edcba".
# follow up:
# Try to solve the problem in O(1) space complexity.


def reverse_string(string):
    # string_without_whitespace = string.replace(' ', '')
    # char_list = [char for char in string_without_whitespace]
    # start = 0
    # end = len(char_list) - 1
    #
    # while start < end:
    #     char_list[start], char_list[end] = char_list[end], char_list[start]
    #     start += 1
    #     end -= 1
    #
    # rev_string = "".join(char_list)
    # return rev_string

    data=list(string)
    length=len(data)

    for i in range(length // 2):
        # print(length,i,1)
        # print(data[i], data[length-i-1])
        data[i],data[length-i-1] = data[length-i-1],data[i]

    return ''.join(data)

# string = "A quick brown fox jumps over the"
string = "Hello"

print(reverse_string(string))
# TIme complexity is 0(n) and Space COplexity is O(1)