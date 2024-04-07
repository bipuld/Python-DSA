'''
Insertion Sort is the sorting algorithm
time complexity: O(n^2) worst case and average time complexity 
best case time complexity: O(n) and Space Complexity is O(1) 
'''

class Sorting():
    
    def insertion(self,arr):
        for i in range(1,len(arr)):
            key=arr[i]
            j=i-1
            while j>=0 and key<arr[j]:
                arr[j+1]=arr[j]
                j-=1
            arr[j+1]=key
            
def fun():
    array=[1,4,5,10,1]
    result=Sorting()
    ans=result.insertion(array)
    print("Array after insertion sort: ",array)
    
    
if __name__ == '__main__':
    fun()