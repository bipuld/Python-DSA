"""
You are given an array 'arr' of length 'n'. Find the index(0-based) of a peak element in the array. If there are multiple peak numbers, return the index of any peak number.
Peak element is defined as that element that is greater than both of its neighbors. If 'arr[i]' is the peak element, 'arr[i - 1]' < 'arr[i]' and 'arr[i + 1]' < 'arr[i]'.
Assume 'arr[-1]' and 'arr[n]' as negative infinity.
Note:
1.  There are no 2 adjacent elements having same value (as mentioned in the constraints).
2.  Do not print anything, just return the index of the peak element (0 - indexed).
3. 'True'/'False' will be printed depending on whether your answer is correct or not.
"""


def array_peak(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        elif arr[mid] > arr[mid + 1]:
            right = mid
        else:
            pass
    return left


array = [1, 2, 1, 4, 5, 6, 7, 5, 2, 10] # number peak is at the 1 index and the  index 8
print(array_peak(array))
