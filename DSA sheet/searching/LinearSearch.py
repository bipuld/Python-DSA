'''
Linear Searching Algorithm is the Searching Algorithm which is used to find the element in the given array
'''

class Searching:
    
    def linear_search(self,arr1):
        key=45
        count=0
        for i in range(len(arr1)):
            if arr1[i]==key:
                count+=1
                return i
        return -1

def arr1():
    array=[5,8,7,9,6,10,23,45]
    res=Searching()
    ans=res.linear_search(array)
    if ans!=-1:
        # print("Element found in the array at index: ",ans)
         print(f"Element 45 found in the array at index: {ans}")
    else:
        print("Element 45 not found in the array")
if __name__ == '__main__':
    arr1()
    
    




# class Searching:
    
#     def linear_search(self, arr, key):
#         for i in range(len(arr)):
#             if arr[i] == key:
#                 return i
#         return -1  # Return -1 if key is not found

# def arr1():
#     array = [5, 8, 7, 9, 6, 10, 23, 45]
#     key_to_search = 45
#     search_instance = Searching()
#     index = search_instance.linear_search(array, key_to_search)
#     if index != -1:
#         print(f"Element {key_to_search} found in the array at index: {index}")
#     else:
#         print(f"Element {key_to_search} not found in the array")

# if __name__ == '__main__':
#     arr1()