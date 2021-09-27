# cook your dish here
from collections import OrderedDict 


for _ in range(int(input())):
    n=int(input())
    arr=list(map(str,input().split()))
    
    og_val = OrderedDict()

    md_val = OrderedDict()
    
    for i in range(len(arr)):
        if(og_val.get(arr[i])==None):
            og_val[arr[i]]=1
        else:
            pass

        head = arr[i][0:1]
        body = arr[i][1:]

        if(md_val.get(body)==None):
            md_val.setdefault(body, [head])
        else:
            tmp = md_val[body]
            if(head not in tmp):
                md_val[body].append(head)
            else:
                pass

    keys_list = list(md_val.keys())
    keys_list = keys_list[1:]
    value_list = list(md_val.values())
    value_list = value_list[:-1]

    count = 0

    for i in value_list:
        if(type(i)==list):
            for j in i:
                for k in keys_list:
                    res = j+k
                    #print(res)
                    if(og_val.get(res)==None):
                        count+=1
                    else:
                        pass
        else:
            for k in keys_list:
                res = i+k
                #print(res)
                if(og_val.get(res)==None):
                    count+=1
                else:
                    pass

    print(2*count)


    #print(md_val)

    #print(keys_list)

    #print(value_list)
        


    # i=0
    # j=len(md_val.keys())

    # for key,val in md_val.items():
    #     tmp = len(val)
    #     tmp2 = len(md_val.keys())
    #     print(tmp,tmp2)
        
