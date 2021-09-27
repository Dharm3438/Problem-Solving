class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        mi = 99999
        
        if(len(strs)==0):
            return ""
        
        c = strs[0]
        
        i=1
        while(i<len(strs)):
            j=0
            k=0
            a=0
            while(j<len(c) and k<len(strs[i])):
                if(c[j]== strs[i][k]):
                    a+=1
                else:
                    break
                j+=1
                k+=1
            mi = min(mi,a)
            i+=1
            
        return c[0:mi]