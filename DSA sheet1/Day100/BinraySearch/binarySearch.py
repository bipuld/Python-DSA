'''You are given an integer array 'A' of size 'N', sorted in non-decreasing order. You are also given an integer 'target'.
Your task is to write a function to search for 'target' in the array 'A'. If it exists, return its index in 0-based indexing. If 'target' is not present in the array 'A', return -1.
Note:
You must write an algorithm whose time complexity is O(LogN)
Example:
Input: ‘N’ = 7 ‘target’ = 3
‘A’ = [1, 3, 7, 9, 11, 12, 45]
Output: 1
Explanation: A = [1, 3, 7, 9, 11, 12, 45],
The index of element '3' is 1.
Hence, the answer is '1'.'''

class Searching:
    
    def binary_search(self,arr1,target):
        num=len(arr1)
        low=0
        high=num-1
        while low <=high:
            mid=(low+high)//2
            mid_value=arr1[mid]
            if target == mid_value:
                return mid
            elif target  >= mid_value:
                low=mid+1
            else:
                high=mid-1
        return -1
    
    
def Search():
    array1=[1,3,7,9,11,12,45]
    target=12
    search=Searching()
    param=search.binary_search(array1,target)
    if param != -1:
        print("{} found at index: {} ".format(target, param))
    else:
        print("{} not found".format(target))

if __name__ == '__main__':
    Search()
                
            
        