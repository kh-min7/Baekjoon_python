import sys

sys.stdin = open("input.txt", "r")

r = float(input())
uclid = r * r * 3.141592653589
taxi = r * r * 2
print(f'{uclid:.6f}')
print(f'{taxi:.6f}')