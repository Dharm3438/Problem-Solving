#code
import math
import sys

for _ in range(int(input())):
    arr = list(map(str,input()))
    n=len(arr)
    
    if(n%2==0):
        pass
    else:
        print(-1)
        continue
    
    stack = []
    
    
    for i in arr:
        if(i=='{'):
            stack.append(i)
        else:
            n = len(stack)
            if(len(stack)<1):
                stack.append(i)
            elif('{'==stack[n-1]):
                stack.pop()
            else:
                stack.append(i)
                
    
    ope = stack.count('{')
    clo = stack.count('}')
    res = math.ceil(ope/2)+math.ceil(clo/2)
    
    print(res)
                
                
            