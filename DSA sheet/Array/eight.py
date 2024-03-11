# You are given an array ‘ARR’ of size ‘N’ containing each number between 1 and ‘N’ - 1 at least once.
# There is a single integer value that is present in the array twice. Your task is to find the duplicate integer
# value present in the array.
# For example:
# Consider ARR = [1, 2, 3, 4, 4], the duplicate integer value present in the array is 4. Hence, the answer is 4 in this case.
# Note :
# A duplicate number is always present in the given array.
# formula for calculation duplicated number is sum(array) -  sum of the first N - 1 natural numbers(N-1)*N/2



def array_input(array,n):
    sum_of_array=sum(array)
    sum_of_n_minus_one_natural_number=((n-1)*n)/2
    duplicated=sum_of_array-sum_of_n_minus_one_natural_number
    return duplicated

array=[1,2,3,4,5,6,7,8,9,9,10,11,12]
num=len(array)
answer=array_input(array,num)
print(answer)