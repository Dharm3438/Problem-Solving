n = input('')
arr = n.split()
n = int(arr[0])
m = int(arr[1])
a = int(arr[2])

b = n//a
p = m//a

if(n%a != 0):
    b=b+1

if(m%a != 0):
    p=p+1

print(p*b)