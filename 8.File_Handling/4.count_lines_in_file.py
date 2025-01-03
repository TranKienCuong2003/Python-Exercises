filename = input()
with open(filename, 'r') as file:
    lines = file.readlines()
    print(len(lines))
