arr = input().split()
scores = input().split()
participant = int(arr[1])
count=0

check_score = int(scores[participant-1])
for item in scores:
    if(int(item) >= check_score and (int(item)!=0 or check_score!=0 )):
        count = count+1
    elif(int(item)<check_score):
        break
print(count)



