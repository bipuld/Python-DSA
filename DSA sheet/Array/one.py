'''
Problem statement
You are given an array of integers 'ARR' of length 'N' and an integer Target. Your task is to return all pairs of elements such that they add up to Target.
Note:
We cannot use the element at a given index twice.
Follow Up:
Try to do this problem in O(N) time complexity. 
'''

from time import time
def sum_pairs(array,target):
    seen=set()
    pairs=[]
    
    for num in array:
        complement=target-num
        
        if complement in seen:
            pairs.append((complement,num))
        else:
            seen.add(num)
    return pairs
def input_array():
    array=input("Enter the array: ")
    target=int(input("Enter the target:"))
    array_input=list(map(int,array.split()))
    return array_input , target


user_input,target=input_array()
start_time=time()
# print("and result is ",sum_pairs(user_input,target),"and execution time is ",(time()-start_time))
result = sum_pairs(user_input, target)
print("Result:", result)
print("Execution time is", (time() - start_time)*1000) 
    