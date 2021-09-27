def party(n):
    #Base case
    if (n==1 or n==2):
        return n

    '''
    Case1 : A goes alone depends of f(n-1)

    Case2 : A goes in pair (n-1)*f(n-2)
    '''

    #recursive assumption
    tmp = party(n-1)+(n-1)*party(n-2)

    #self work
    return tmp

if __name__ == "__main__":
    n = int(input('Enter a Number: '))
    print(party(n))