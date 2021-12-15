result = 0
def binary_search(array, start, end):
    global result
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for i in array:
            cnt += i // mid
        if cnt < n:
            end = mid - 1
        else:
            result = mid
            start = mid + 1


k, n = map(int, input().split())
array = []
for _ in range(k):
    array.append(int(input()))

ans = binary_search(array, 1, max(array))
print(result)