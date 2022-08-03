k, n, m = map(int, input().split())

diff = m-(k*n)
if diff <0:
  print(abs(diff))
else:
  print(0)