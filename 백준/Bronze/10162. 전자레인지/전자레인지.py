time = int(input())
a=b=c=0

if time % 10 != 0:
  print(-1)
else:
  a = time // 300
  b = (time%300) // 60
  c = ((time%300)%60)//10

  print(a,b,c)
