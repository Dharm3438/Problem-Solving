def solve(strings):
    word = "hello"
    index = 0
    for i in range(0,len(strings)):
        if(index==5):
            return "YES"
        if(strings[i]==word[index]):
            index+=1

    if(index<5):
        return "NO"
    else:
        return "YES"



if __name__ == "__main__":
    strings = input()
    print (solve(strings))