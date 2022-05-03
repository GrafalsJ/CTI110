user_int = int(input('Enter integer (32 - 126):\n'))


userfloat = float(input('Enter float:\n'))
userchar = input('Enter character:\n')
userstr = str(input('Enter string:\n'))


print(user_int, userfloat, userchar, userstr)
print(userstr,userchar,userfloat,user_int)
inttochr = chr(user_int)
print(user_int, 'converted to a character is',inttochr)
