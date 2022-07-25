hour, minute, second = map(int, input().split())
time = int(input())

second += time % 60
time = time // 60
if second >= 60:
  second -= 60
  minute += 1

minute += time % 60
time = time // 60
if minute >= 60:
  minute -= 60
  hour += 1

hour += time % 24
if hour >= 24:
  hour -= 24

print(hour,minute,second)