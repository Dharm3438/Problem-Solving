def subs(val,output):
    if(val==''):
        output[0]=''
        return 1

    smallstr = val[1:]
    smalloptsize = subs(smallstr,output)
    for i in range(1,smalloptsize):
        output[i+smalloptsize] = val[0]+output[i]

    return 2*smalloptsize
