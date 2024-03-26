def merge_arrays(arr1, arr2, m, n, i):
    """
  Merges two sorted arrays `arr1` and `arr2` into `arr1` in-place.

  Args:
      arr1: The first sorted array with extra space to hold elements of `arr2`.
      arr2: The second sorted array.
      m: The size of the first array (excluding extra space).
      n: The size of the second array.

  Returns:
      None (modifies `arr1` in-place).
  """

    if n == 0 and i == m + n:
        return
    if arr1[i - 1] > arr2[n - 1]:
        arr1[i] = arr1[i - 1]
        merge_arrays(arr1, arr2, m, n, i + 1)
    else:
        arr1[i] = arr2[n - 1]
        merge_arrays(arr1, arr2, m, n - 1, i + 1)


# Example usage
arr1 = [3, 6, 9, 0, 0]
arr2 = [4, 10]
m = len(arr1) // 2
n = len(arr2)
i = m + n
merge_arrays(arr1, arr2, m, n, i)

print(arr1)
