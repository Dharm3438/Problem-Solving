for _ in range(int(input())):
    main_str = input()
    sub_str = input()
    temp_str = main_str

    for i in sub_str:
        pos = main_str.find(i)
        main_str = main_str[:pos] + main_str[pos+1:]
        
    res_str = ''.join(sorted(main_str))
    
    pos = len(res_str)
    
    for j in range(len(res_str)):
        if(sub_str[0]<res_str[j]):
            #print(f"pos {j}")
            pos = j
            break
            
    final_str=res_str[:pos] + sub_str + res_str[pos:]
    print(final_str)