test=[]
month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
people = []
for j in range(1,12+1):
    for i in range(1,month[j]+1):
        test.append((6-j)**2+abs(i-15))
        #print(f"j: {j} month[j]: {month[j]}")
    people.append(sum(test))
    test = []

print(month)
print(people)
print(sum(people))