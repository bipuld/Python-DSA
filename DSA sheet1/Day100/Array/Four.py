class solution_ans:
    def generate(self,num:int):
        res=[[1]]
        
        for i in range(num-1):
            temp=[0]+res[-1]+[0]
            row=[]
            for j in range(len(res[-1])+1):
                row.append(temp[j]+temp[j+1])
            res.append(row)
            return res