def func(s, p):
    if s == p or p == '*':
        return True
    if len(s) == len(p):
        for i in range(len(s)):
            if(s[i] != p[i] and p[i]!='?'):
                return False
        return True
    else:
        return False

s = input()
p = input()
print(func(s, p))