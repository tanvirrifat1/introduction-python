n, q = map(int, input().split())
a = list(map(int, input().split()))

# prefix sum array
prefix = [0]

for num in a:
    prefix.append(prefix[-1] + num)

# queries
for _ in range(q):
    l, r = map(int, input().split())
    print(prefix[r] - prefix[l - 1])
