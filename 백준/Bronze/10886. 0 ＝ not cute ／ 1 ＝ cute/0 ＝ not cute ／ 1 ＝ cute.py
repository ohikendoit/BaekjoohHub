count = int(input())

cute = 0

for i in range(count):
  if int(input()) == 1:
    cute += 1
  
if cute > count//2:
  print('Junhee is cute!')
else:
  print('Junhee is not cute!')