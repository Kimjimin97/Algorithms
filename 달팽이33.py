n, m = map(int,input().split())
d = (min(n, m) - 1) // 2
ans = 4*d
row = 1+d
col = 1+d
n -= 2*d
m -= 2*d

if n == 1:
    col += (m - 1)
elif m == 1:
    ans += 1
    row += (n - 1)
elif n == 2:
    ans += 2
    row += 1
else:
    ans += 3
    row += 1
print(ans)
print('%d %d' % (row, col))