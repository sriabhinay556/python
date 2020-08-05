number=int(input("Enter number between 100 and 1000:"))
remainder=0
sumdigit=0
if(number>=100 and number<=1000):
    while number > 0:
      remainder=number%10
      sumdigit=sumdigit+remainder
      number=number//10
print(sumdigit)
