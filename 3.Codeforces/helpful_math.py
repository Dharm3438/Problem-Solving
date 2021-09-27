values = input().split('+')
values.sort()

final_str = ''

for i in values:
    final_str = final_str + '+' + i

final_str = final_str[1:]

print(final_str)