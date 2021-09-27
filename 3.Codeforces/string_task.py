
name = list(map(str, input().lower()))

new_name = []
final_str =''
no_vowels = name.copy()


for i in name:

    if(i == 'a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='y'):
        #print(i)
        no_vowels.remove(i)

for i in no_vowels:
    new_name.append('.')
    new_name.append(i)

for i in new_name:
    final_str += i

print(final_str)