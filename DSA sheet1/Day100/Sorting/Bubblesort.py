'''
Bubble Sorting is the Sorting algorithm  
timeComplexity O(n^2) worst case and average case
best case: O(n)
Space Complexity o(n)
'''

class Sorting():
    
    def bubble_sorting(self,array):
        n=len(array)
        swap=False
        for i in range(n):
            for j in range(0,n-i-1):
                if array[j]>array[j+1]:
                    array[j],array[j+1]=array[j+1],array[j]
                    swap=True
            if not swap:
                break
    
def array_pass():
    array=[1,4,5,6,7,8,9,0,3,4]
    sorted=Sorting()
    sorting_array=sorted.bubble_sorting(array)
    print(array)
    
if  __name__ == '__main__':
    array_pass()
    