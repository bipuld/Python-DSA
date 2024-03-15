'''Searching Algorithm: Binary Search
Time Complexity: O(log n)
'''
import math

class Searching:
    
    def binary_search(self,arr1,value):
        num=len(arr1)
        lower_index=0
        upper_index=num-1
        while lower_index <= upper_index:
            mid_index=math.floor(lower_index+upper_index/2)
            array_mid=arr1[mid_index]
            if array_mid == value:
                return mid_index
            elif array_mid < value:
                lower_index=mid_index+1
            else:
                upper_index=mid_index-1
         
        return -1
        


def value():
    array1=[1,2,3,4,5,6,7,8,9,10]
    search=Searching()
    item_search=188
    param=search.binary_search(array1,item_search)
    if param != -1:
        print("{} found at index: {} ".format(item_search, param))
    else:
        print("{} not found".format(item_search))
        
if __name__ == '__main__':
    value()