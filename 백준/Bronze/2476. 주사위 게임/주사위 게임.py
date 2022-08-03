n = int(input())

result = []

for i in range(n):
  a, b, c = map(int, input().split())
  
  if a==b==c:
    value=10000+a*1000
    result.append(value)
  elif a==b or a==c:
    value=1000+a*100
    result.append(value)
  elif b==c:
    value=1000+b*100
    result.append(value)
  else:
    value=max(a,b,c)*100
    result.append(value)

result.sort()
print(result[-1])