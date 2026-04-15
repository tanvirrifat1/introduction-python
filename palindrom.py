n = int(input())
a = list(map(int, input().split()))


i = 0
j = n - 1

is_palindrome = True

while i < j:
    if a[i] != a[j]:
        is_palindrome = False
        break
    i += 1
    j -= 1

if is_palindrome:
    print("YES")
else:
    print("NO")
