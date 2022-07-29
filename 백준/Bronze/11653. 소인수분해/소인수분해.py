input = int(input())

start = 2

while input != 1:
  if input % start == 0:
    input = input / start
    print(start)
  else:
    start += 1