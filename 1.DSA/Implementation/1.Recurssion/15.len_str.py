def len_str(n):
    if(n==''):
        return 0

    return 1+len_str(n[1:])


print(len_str('a'))
print(len_str('ab'))
print(len_str('abc'))
print(len_str('abcd'))