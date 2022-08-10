count = int(input())

cy = sd = 100

for i in range(count):
  a, b = map(int, input().split())
  if a > b:
    sd -= a
  elif a < b:
    cy -= b

print(cy, sd, sep="\n")