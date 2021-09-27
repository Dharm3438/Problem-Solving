stops = int(input())
first_stop = list(map(int, input().split()))
entered = first_stop[1]
entered_values = []
entered_values.append(entered)

for i in range(stops-1):
    temp_stop = list(map(int, input().split()))
    temp_exited = temp_stop[0]
    temp_entered = temp_stop[1]

    entered = entered - temp_exited + temp_entered
    entered_values.append(entered)


print(max(entered_values))
