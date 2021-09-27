def pow(a,b):
    #base case
    if(b==0):
        return 1

    #recursive assumption
    tmp = a*pow(a,b-1)

    #self work
    return tmp

if __name__ =="__main__":
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))

    print(pow(a,b))
