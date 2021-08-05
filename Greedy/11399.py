total_people = int(input())
people_list = list(map(int, input().split()))
people_list.sort()

ans = 0
ans2 = 0


for i in people_list:
    ans += i
    ans2 += ans

print(ans2)


# list에서 map 사용법 확인