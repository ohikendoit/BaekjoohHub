while True:
  number = int(input())
  if number == -1:
    break

  result = []
  for i in range (1, number):
    if number % i == 0:
      result.append(i)
  
  if sum(result) == number:
    print(number, " = ", " + ".join(str(i) for i in result), sep="")
  else:
    print(number, "is NOT perfect.")