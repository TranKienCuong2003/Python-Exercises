filename = input()
content = input()
with open(filename, 'w') as file:
    file.write(content)
