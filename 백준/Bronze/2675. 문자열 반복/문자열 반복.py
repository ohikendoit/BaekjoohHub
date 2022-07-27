case = int(input())

for i in range(case):
  count, word = input().split()
  for x in word:
    print(x*int(count), end='')
  print()