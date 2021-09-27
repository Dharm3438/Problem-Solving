
def dec(n):
    #Base Case
    if(n<=0):
        return

    #Self Work
    print(n,end=' ')

    #Recursive Assumption
    dec((n-1))

if __name__ == '__main__':
    n = int(input('Enter a Number: '))
    dec(n)