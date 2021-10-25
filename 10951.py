import sys

sys.stdin = open("input.txt", "r")

""" try-except문 """

while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break

