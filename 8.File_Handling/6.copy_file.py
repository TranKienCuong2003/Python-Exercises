source = input()
destination = input()
with open(source, 'r') as file:
    content = file.read()
with open(destination, 'w') as file:
    file.write(content)
