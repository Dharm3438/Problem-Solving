
def number(n):
    #Base Case
    if(n<=0):
        return

    #Recursive Assumption
    number(n-1)
    
    #Self Work
    print(n, end=' ')
    

if __name__ =='__main__':
    n = int(input('Enter a Number: '))
    number(n)