# https://codeforces.com/contest/1369/problem/C

n = int(input())

for _ in range(n):
    n_integers, n_friends = list(map(int, input().split()))
    integers = list(map(int, input().split()))
    gifts = list(map(int, input().split()))

    integers = sorted(integers, reverse=True)
    gifts = sorted(gifts)

    happiness_total = 0

    for i in range(n_friends):
        happiness_total += integers[i]
        if gifts[i] == 1:
            happiness_total += integers[i]

    i = n_friends - 1
    for gift in gifts:
        if gift != 1:
            i += gift - 1
            happiness_total += integers[i]

    print(happiness_total)