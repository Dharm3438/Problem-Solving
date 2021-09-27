n1, n2 = map(int,input().split())
prime1 = []
comb = []
prime2 = []
for i in range(n1,n2+1):
  if(i>1):
    if(i==2):
      prime1.append(i)
    for j in range(2,i//2+2):
      if(i%j==0):
        break
      else:
        if(j==i//2+1):
          prime1.append(i)
k=0
for k in range(len(prime1)):
  for l in range(len(prime1)):
    if(str(prime1[k]) == str(prime1[l])):
      continue
    res = str(prime1[k]) + str(prime1[l])
    comb.append(int(res))
for m in comb:
  if(m>1):
    if(m==2):
      prime2.append(m)
    for n in range(2,m//2+2):
      if(m%n==0):
        break
      else:
        if(n==m//2+1):
          if(m not in prime2):
            prime2.append(m)
terms = len(prime2)
start = min(prime2)
end = max(prime2)
# USing DP for fibonacci
fibo = [start,end]
def nth_fibo(n):
  if n<0:
    return -1
  elif n<=len(fibo): 
    return fibo[n-1] 
  else:
    temp = nth_fibo(n-1)+nth_fibo(n-2) 
    fibo.append(temp) 
  return temp
print(nth_fibo(terms))
