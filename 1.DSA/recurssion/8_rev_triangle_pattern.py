
def pattern(r,c):
    #base case
    if (r==0):
        return

    if(c<r):
        print('*', end=' ')
        pattern(r,c+1)
    else:
        print()
        pattern(r-1,0)


if __name__ == '__main__':
    n = int(input('Enter a number: '))
    pattern(n,0)