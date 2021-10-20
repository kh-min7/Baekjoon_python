T = int(input())
for i in range(T):
    floor = int(input())
    room = int(input())
    people = [j for j in range(1, room+1)]
    for k in range(floor):
        for v in range(room-1):
            people[v+1] += people[v]
    print(people[-1])
