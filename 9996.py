n = int(input())

first = input().split('*')
front = first[0]
back = first[1]

for _ in range(n):
  s = input()
  if s[:len(front)] == front and s[-len(back):] == back and len("".join(first)) <= len(s):
    print("DA")
  else:
    print("NE")
