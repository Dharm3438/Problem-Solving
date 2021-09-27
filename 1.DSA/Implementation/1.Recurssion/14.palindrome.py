def helper(n,start,end):

    if(end-start<1):
        return True

    if(n[start]==n[end]):
        return helper(n ,start+1,end-1)
    else:
        return False

def palindrome(n):
    return helper(n,0,len(n)-1)

print(palindrome('a'))
print(palindrome('aa'))
print(palindrome('ab'))
print(palindrome('aba'))
print(palindrome('abc'))
print(palindrome('abba'))
print(palindrome('abda'))
