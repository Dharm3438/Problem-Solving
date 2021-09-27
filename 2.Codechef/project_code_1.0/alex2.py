# n = int(input())
# k = int(input())
# count = 0
# a = 0
# while(count !=k):
#     for i in range(n):
#         if count == k:
#             print(a+i)
#             break
#         else:
#             count = count+1
    
#     a = a+1
    
#print(i)
n = int(input())
k = int(input())
count = 0
a = 0
while(count !=k):
    for i in range(n):
        if count == k:
            a = a + 1
            break
        else:
            count = count+1
    
    a = a+1
print(a)