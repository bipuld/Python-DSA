'''You are given an array A of length N, where N is always an odd integer. There are (N-1)/2 elements in the array that occur twice and one element which occurs once.

Your task is to find the only element that occurs once in the array.
j
Note: There are (N-1)/2+1 elements that are unique in the array.
'''

def check_uniqueness(array):
    unique_set=set()
    print("Type",type(unique_set))
    
    for num in array:
        if num in unique_set:
            unique_set.remove(num)
        else:
            unique_set.add(num)
        
    return unique_set.pop()

array=[3,5,5,8,8,9,9]
result=check_uniqueness(array)
print("The uniqueness number that is  in the Array is",result)