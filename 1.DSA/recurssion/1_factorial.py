
def factorial(n):
    #Base Case
    if(n==1):
        return 1
    
    #Recursive assumption
    tmp = n*factorial(n-1)
    
    #Self work
    return tmp


if __name__ == "__main__":
    n = int(input('Enter a number: '))
    print(factorial(n))