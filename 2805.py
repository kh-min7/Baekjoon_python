n, m = map(int, input().split())

array = (list(map(int, input().split())))

start = 0
end = max(array)

result = 0
while start <= end:
    mid = (start + end) // 2
    cnt = 0

    for x in array:
        if x > mid:
            cnt += x - mid

    if cnt >= m:
        result = mid
        start = mid + 1
    elif cnt < m:
        end = mid - 1

print(result)
