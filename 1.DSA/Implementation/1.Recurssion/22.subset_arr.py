def permutationFind(input,output):
        if(input==''):
            print(output)
            return
        
        out1 = output
        out2 = output
        out2 += input[0]
        input = input[1:]

        permutationFind(input,out1)
        permutationFind(input,out2)
    

permutationFind('123','')