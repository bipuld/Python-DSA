"""
Ninja has been given two sorted integer arrays/lists ‘ARR1’ and ‘ARR2’ of size ‘M’ and ‘N’. Ninja has to merge these sorted arrays/lists into ‘ARR1’ as one sorted array. You may have to assume that ‘ARR1’ has a size equal to ‘M’ + ‘N’ such that ‘ARR1’ has enough space to add all the elements of ‘ARR2’ in ‘ARR1’.

For example:

‘ARR1’ = [3 6 9 0 0]
‘ARR2’ = [4 10]
After merging the ‘ARR1’ and ‘ARR2’ in ‘ARR1’.
‘ARR1’ = [3 4 6 9 10]
Using recyrsion
"""


def merge_arr_to_arr(arr1, arr2):
    m = len(arr1) - 1
    n = len(arr2) - 1
    p = m + n - 1

    while m >= 0 and n >= 0:
        if arr1[m] > arr2[n]:
            arr1[p] = arr1[m]
            m -= 1
        else:
            arr1[p] = arr2[n]
            n -= 1
        p -= 1

    # If there are remaining elements in arr2, copy them to arr1
    while n >= 0:
        arr1[p] = arr2[n]
        n -= 1
        p -= 1


# Example usage:
arr1 = [3, 6, 9, 0, 0]
arr2 = [4, 10]
merge_arr_to_arr(arr1, arr2)
print(arr1)  # Output: [3, 4, 6, 9, 10]
