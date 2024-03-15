
'''
You are given an array 'ARR' of integers. Your task is to modify the array so that all the array elements having zero values get pushed to the left and all the array elements having non-zero value come after them while maintaining their relative order.

For example :

Explain
Consider the array { 1, 1, 0, 2, 0 }. 
For the given array the modified array should be {0,0,1,1,2} . 
'''
class Solution:
    
    def rearrange_array(self, arr):
        
        left_pointer = 0
    
        for current_pointer in range(len(arr)):
            if arr[current_pointer] == 0:
                arr[current_pointer], arr[left_pointer] = arr[left_pointer], arr[current_pointer]
                left_pointer += 1
        return arr

if __name__ == "__main__":
    array = [0, 2, 0, 3, 4, 0, 5, 0]
    arr = Solution()
    result = arr.rearrange_array(array)
    print(result)
