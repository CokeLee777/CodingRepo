input_s = str(input())
s = []
for i in range(len(input_s)):
    s.append(input_s[i])
    if i == len(input_s) - 1:
        s.append(s[i])

print(s)