def increasing_decreasing(n):
    #base case
    if(n==1):
        print(n, end=' ')
        return

    #self work
    print(n, end=' ')

    #recursive assumption
    increasing_decreasing(n-1)

    #selfwork
    print(n, end=' ')
    

if __name__ == '__main__':
    n = int(input("Enter a Number: "))
    increasing_decreasing(n)