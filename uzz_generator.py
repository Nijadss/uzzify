def uzz(s):
    if s[0] == 'A' or s[0] == 'a':
        if s[1] == 'u':
            return s[0]+s[1]+s[2]+'uzz'
    else:
        return s[0]+'uzz'
s = input()
print(uzz(s))