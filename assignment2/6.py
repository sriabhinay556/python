sal = float(input("Enter salary : "))
if(sal <= 250000):
    print("Nil")
elif(sal > 1500000):
    print("30 percent")
else:
    x = 250000
    c = 0
    while(x <= 1500000):
        if((x+1) <= sal <= (x+250000)):
            c = c+1
            print(c*5, "percent")
            break
        x = x+250000
        c = c+1
