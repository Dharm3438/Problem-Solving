#User function Template for python3
'''
Function Arguments :
		@param  : s (given string containing parenthesis) 
		@return : boolean True or False
'''
def ispar(x):
    # code here
    stack = []
    val,val2=0,0
    
    for i in x:
        if(i=='(' or i=='[' or i=='{'):
            stack.append(i)
        else:
            n = len(stack)
            if(n<1):
                return False
            val = stack[n-1]
            if(i==')'):
                val2='('
            elif(i==']'):
                val2='['
            elif(i=='}'):
                val2='{'
                
            if(val2==val):
                stack.pop()
            else:
                return False
            
        #print(stack,i,val,val2,val3)
              
  
    if(len(stack)==0):
        return True
    else:
        return False

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

#Contributed by : Nagendra Jha


_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        #n = int(input())
        #n,k = map(int,imput().strip().split())
        #a = list(map(int,input().strip().split()))
        s = str(input())
        if ispar(s):
            print("balanced")
        else:
            print("not balanced")
# } Driver Code Ends