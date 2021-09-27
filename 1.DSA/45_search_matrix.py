class Solution:
def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col = len(matrix[1])
        row = len(matrix)
        
        i=0
        j=0
        
        arr=[]
        
        for i in range(0,row):
            arr.append(matrix[i][j])
          
        
        for i in range(len(arr)-1,-1,-1):
            if(target<arr[i]):
                pass
            else:
                val=i
                
        flg=0
        
        for i in matrix[val]:
            if i==target:
                flg = 1
            
                    
        if(flg==1):
            print("true")
        else:
            print("false")