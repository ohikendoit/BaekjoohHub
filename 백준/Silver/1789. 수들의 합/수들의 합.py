input = int(input())

count = 0
result = 0

for i in range(1, input+1):
  result += i
  count += 1
  if (result > input):
    count -= 1
    break
print(count)