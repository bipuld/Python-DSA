class Solution:
    # Boyer-More-Voting Algorithm
    
    def counting_system(self,array):
        candidate=None
        count=0
        for num in array:
            
            if count==0:
                candidate=num
            count +=1 if num==candidate else -1
            
            
            # 2 phase verifying phase
            count=0
        for num in array:
            if num == candidate:
                count +=1
                
        # 3 phase comparison phase
        if count > len(array)//2:
            return candidate
        else:
            return -1
            
def ans():
    arr = [3, 3, 4, 2, 4, 4, 2, 4, 4]
    res=Solution()
    ans=res.counting_system(arr)
    print(ans)
    
if __name__ == "__main__":
    ans()
                  