import csv
filename = input()
data = [list(map(str, input().split())) for _ in range(int(input()))]
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
