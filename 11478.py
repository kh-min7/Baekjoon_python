s = input()
e = set()

for i in range(len(s)):
  for j in range(i, len(s)):
    e.add(s[i:j+1])
print(len(e))