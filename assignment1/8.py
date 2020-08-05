for number in range(0,1001):
  temp=number
  rev=0
  if(number>=100 and number<=1000):
    while temp > 0:
      rem=temp%10
      rev=(rev*10)+rem
      temp=temp//10
    if number==rev:  
      print(number ,end=" ")
