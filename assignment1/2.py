print("enter distance to be travelled",end=" ")
d=int(input())
print("enter weight of goods",end=" ")
w=int(input())
if(d>=500):
    if(w>=100):
        c=5
    elif(w>=10 and w<100):
        c=6
    else:
        c=7
else:
    if(w>=100):
        c=8
    else:
        c=5
print(f'amount to be charged : {d*c}')
