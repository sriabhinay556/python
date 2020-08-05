for number in range(1,1001):
  sum=0
  temp=number
  while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
  if number==sum:
    print(number,end=" ")
