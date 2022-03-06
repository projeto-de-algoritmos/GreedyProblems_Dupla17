# Link do problema  https://www.spoj.com/problems/BUSYMAN/

n = int(input())

for _ in range(n):
    number_activities = int(input())

    activities_time = []
    for _ in range(number_activities):
        start, end = list(map(int, input().split()))
        activities_time.append([start, end])

    activities_time = sorted(activities_time, key=lambda activitie: activitie[1])

    maximum_activities = []
    for start, end in activities_time:
        if len(maximum_activities) == 0:
            maximum_activities.append([start, end])
        elif start >= maximum_activities[-1][1]:
            maximum_activities.append([start, end])

    print(len(maximum_activities))
