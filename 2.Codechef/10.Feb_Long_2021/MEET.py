# cook your dish here
def convert_time(arr):
    tmp1 = arr[0]
    val1 = tmp1.split(':')[0]
    val2 = tmp1.split(':')[1]
    form = arr[1]
    if(form=='AM'):
        if(val1=='12'):
            fin = '00' + val2
        else:
            fin = val1 + val2
    else:
        if(val1=='12'):
            fin = val1 + val2
        else:
            tmp = int(val1)
            tmp = str(tmp+12)
            fin = tmp + val2
            
    return int(fin)
    

for _ in range(int(input())):
    
    frnd_time = list(map(str,input().split()))
    frnd_val = convert_time(frnd_time)
    
    n = int(input())
    res = ''
    
    for i in range(n):
        meet = list(map(str,input().split()))
        start = convert_time(meet[:2])
        end = convert_time(meet[2:])
        
        if(start<=frnd_val and frnd_val<=end):
            res += '1'
        else:
            res += '0'
    
    print(int(res))