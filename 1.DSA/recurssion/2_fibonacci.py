def fib(n):
    #Base Case
    if(n==0 or n==1):
        return n

    #recursive assumption
    tmp1 = fib(n-1)
    tmp2 = fib(n-2)

    #self work
    return tmp1+tmp2

    

if __name__ == '__main__':
    n = int(input('Enter a Number: '))
    print(fib(n))