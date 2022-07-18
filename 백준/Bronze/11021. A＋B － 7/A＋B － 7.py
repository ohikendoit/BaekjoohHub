cases = int(input())

for i in range(cases):
    n,m = map(int, input().split())
    ans = n+m
    print("Case #%s: %s"%(i+1, ans))