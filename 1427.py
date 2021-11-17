import sys

sys.stdin = open("input.txt", "r")

n = list(input())
n.sort(reverse=True)
a = ''
for i in n:
    a += i

print(a)

"""
end=''
"""
