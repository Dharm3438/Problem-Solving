dimensions = list(map(int, input().strip().split()))

area = dimensions[0] * dimensions[1]

no_of_domino = area // 2

print(no_of_domino)