num = int(input())

for i in range(num):
    word = input('')
    if(len(word)>10):
        abbr = word[0]
        abbr = abbr + str(len(word)-2)
        abbr = abbr + word[-1]
        print(abbr)
    else:
        print(word)