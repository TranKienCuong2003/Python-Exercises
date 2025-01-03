filename = input()
numbers = list(map(int, input().split()))
with open(filename, 'w') as file:
    for number in numbers:
        file.write(str(number) + '\n')
