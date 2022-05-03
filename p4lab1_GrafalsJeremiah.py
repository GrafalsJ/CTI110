user_text = input()
count = 0
for character in user_text:
    if character == '.' or character == ' ' or character == '!' or character == ',':
        count = count
    else:
        count += 1
print(count)
