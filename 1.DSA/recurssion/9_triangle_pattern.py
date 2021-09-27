def pattern(r,c):
    #base case
    if (r==0):
        return

    if(c<r):
        pattern(r,c+1)
        print('*', end=' ')
    else:
        pattern(r-1,0)
        print()


if __name__ == '__main__':
    n = int(input('Enter a number: '))
    pattern(n,0)