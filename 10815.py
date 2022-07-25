n = int(input())
arr = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

arr.sort()

def binary(list, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    if target == list[mid]:
      return target
    elif target < list[mid]:
      end = mid - 1
    else:
      start = mid + 1
  
  return None

for i in range(m):
  if binary(arr, arr2[i], 0, n - 1):
    print(1, end=" ")
  else:
    print(0, end= " ")