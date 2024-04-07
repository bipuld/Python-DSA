"""The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above."""


class Solution:

    def greater_element(self, num1, num2):
        stack = []
        next_greater_element = {}

        for num in num2:
            # Find next greater element for each number in nums2
            while stack and stack[-1] < num:
                next_greater_element[stack.pop()] = num
                # print("Hello", stack)
            stack.append(num)
        for num in stack:  # if no grater element in the stack simply assign the -1
            next_greater_element[num] = -1

        ans = [next_greater_element[num] for num in num1]

        return ans
if __name__ == '__main__':
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    value = Solution()
    print(value.greater_element(nums1, nums2))
