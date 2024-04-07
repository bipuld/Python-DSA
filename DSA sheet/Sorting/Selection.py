'''
Selection Sort is the Sorting Algorithm

Time Complexity O(n^2) worst case and average case O(n^2)
best case O(n^2)

Space Complexity is O(1) 

'''
class Sorting():
    
    def selection(self, array):
        n = len(array)

        for i in range(n-1):
            mini = i
            for j in range(i+1, n):
                if array[j] < array[mini]:
                    mini = j

            # Swap elements
            array[i], array[mini] = array[mini], array[i]

def array_input():
    array = [1, 8, 0, 5, 9, 2, 6]
    sort = Sorting()
    sort.selection(array)
    print(array)

if __name__ == '__main__':
    array_input()
