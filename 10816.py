from bisect import bisect_left, bisect_right


def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index


n = int(input())
A = list(map(int, input().split()))
A.sort()
m = int(input())
B = list(map(int, input().split()))

for i in B:
    print(count_by_range(A, i, i), end=" ")