judge = int(input())
vote = list(str(input()))

A = 0
B = 0

for i in vote:
  if i == 'A':
    A+=1
  else:
    B+=1

if A>B:
  print('A')
elif B>A:
  print('B')
else:
  print('Tie')