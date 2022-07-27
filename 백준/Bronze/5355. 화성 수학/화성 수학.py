case = int(input())

for i in range(case):
  var = list(map(str, input().split()))
  answer = 0
  for i in range(len(var)):
      if i == 0:
        answer += float(var[i])
      else:
        if var[i] == '@':
          answer *= 3
        elif var[i] == '%':
          answer += 5
        elif var[i] == '#':
          answer -= 7
      
  print("%0.2f" % answer)