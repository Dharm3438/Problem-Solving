def even(n):
    if(n<=0):
        return

    even(n-1)
    
    if(n%2==0):
        #For Even
        #print(n, end=' ')
        pass
    else:
        #For Odd
        print(n, end=' ')
        pass


if __name__ == '__main__':
    n = int(input('Enter a Number: '))
    even(n)