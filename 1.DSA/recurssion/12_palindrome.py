def reverse(n,i,osf):
    #global osf
    if(i<0):
        return
    
    #osf.append(n[i])
    osf+=n[i]
    reverse(n,i-1,osf)

    return osf



if __name__ == '__main__':
    osf = []
    n = input('Enter a String: ')
    print(reverse(n,len(n)-1,''))
    #print(osf)
    #if(n==osf):
    #    print('True')
    #else:
    #    print('False')