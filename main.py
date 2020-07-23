def fib(num):
  
  digit0 = 0

  digit1 = 0

  cursum = digit0 + digit1

  print(cursum)

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

    
 

fib(20)