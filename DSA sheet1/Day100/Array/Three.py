'''
Ninja has been given two sorted integer arrays/lists ‘ARR1’ and ‘ARR2’ of size ‘M’ and ‘N’. Ninja has to merge these sorted arrays/lists into ‘ARR1’ as one sorted array. You may have to assume that 
‘ARR1’ has a size equal to ‘M’ + ‘N’ such that ‘ARR1’ 
has enough space to add all the elements of ‘ARR2’ in ‘ARR1’.
'''
def merge_array(a1, a2, m, n):
    i = m - 1
    j = n - 1
    k = m + n - 1

    while i >= 0 and j >= 0:
        if a1[i] > a2[j]:
            a1[k] = a1[i]
            i -= 1
        else:
            a1[k] = a2[j]
            j -= 1
        k -= 1

    while j >= 0:
        a1[k] = a2[j]
        j -= 1
        k -= 1

# Example usage

a1 = [1, 8, 8, 9, 5, 0, 0, 0]  # Increased size to m + n
a2 = [5, 4, 6, 80]
m = 4  # Increased to the actual size of a1
n = 4  # Increased to the actual size of a2

merge_array(a1, a2, m, n)

# Print the merged array
print(a1)
