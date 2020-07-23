def fib(num):

  digit0 = 0
  digit1 = 0
  cursum = digit0 + digit1

  print(cursum)

  #The first print happens outside of the range loop, thus the range must have an iteration subtracted to arrive to the actual number passed as the parameter.

  for i in range(num - 1):
      
      if i == 0:
      
        digit1 += 1
        cursum = digit0 + digit1
        print(cursum)

      else:
        cursum = digit0 + digit1
        digit0 = digit1
        digit1 = cursum
        print(cursum)


fib(200)