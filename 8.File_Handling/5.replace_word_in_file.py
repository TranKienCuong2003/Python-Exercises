filename = input()
old_word = input()
new_word = input()
with open(filename, 'r') as file:
    content = file.read()
content = content.replace(old_word, new_word)
with open(filename, 'w') as file:
    file.write(content)
