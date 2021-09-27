
def binToDec(n): 
    return int(n,2) 

for _ in range(int(input())):
    n = int(input())
    bin_val = bin(n)[2:]
    
    A='1'
    B='0'

    i=1
    while(i<len(bin_val)):
        if(bin_val[i]=='1'):
            A+='0'
            B+='1'
        else:
            A+='1'
            B+='1'
        i+=1

    val1 = binToDec(A)
    val2 = binToDec(B)
    print(val1*val2)

