# for _ in range(int(input())):
#     s, n = map(int, input().split())
#     ct = 0
#     rem = 1

#     if(s == n):
#         if(s % 2 == 0):
#             ct = 1
#         elif(s==1):
#             ct = 1
#         else:
#             ct = 2
#     elif(s < n):
#         if(s % 2 == 0):
#             ct = 1
#         elif(s==1):
#             ct = 1
#         else:
#             ct = 2
#     elif(s > n):
#         if(n % 2 == 0):
#             while(rem > 0):
#                 if(n == 0):
#                     n = 1
#                 rem = s % n
#                 ct += s//n
#                 temp = s//n
#                 val = temp * n
#                 s = s - val
#                 n = n-2

#     else:
#         n = n-1
#         while(rem > 0):
#             if(n == 0):
#                 n = 1
#             rem = s % n
#             ct += s//n
#             temp = s//n
#             val = temp * n
#             s = s - val
#             n = n-2

#     print(ct)

for _ in range(int(input())):
    s, n = map(int, input().split())  # 31 4

    remainder = s % n  # 1
    quotient = s//n  # 7
    remaining = s-(quotient*n)  # 3
    flag = 0
    if remainder == 0:
        flag = 1
    else:
        while s > 0:

            if remaining > 1:
                remaining = remaining % 2
                quotient += 1
                s = remaining
                flag = 1
            else:
                # print(quotient+1)
                s = 0
                flag = 0
    if flag == 1:
        print(quotient)
    else:
        print(quotient+1)
