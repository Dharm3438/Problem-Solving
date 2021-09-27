#code
for _ in range(int(input())):
    
    s = input()
    
    start=0
    end=1
    
    for i in range(1,len(s)):
        
        
        ##even palindrome part logic
        l=i-1
        h=i
        
        while(l>=0 and h<len(s) and s[l]==s[h]):
            if(h-l+1>end):
                start = l
                end = h-l+1
            
            l-=1
            h+=1
        
        
        ##odd palindrome part logic
        l=i-1
        h=i+1
        
        while(l>=0 and h<len(s) and s[l]==s[h]):
            if(h-l+1>end):
                start = l
                end = h-l+1
            
            l-=1
            h+=1
            
    print(s[start:start+end])
        
        