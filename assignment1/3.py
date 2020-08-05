print("enter Type of seat : ",end="")
s=input()
print("enter Payment Mode")
p=input()
if(s.lower()=="stalls"):
    c=625
elif(s.lower()=="circle"):
    c=750
elif(s.lower()=="upper class"):
    c=850
else:
    c=1000

if(p.lower()=="cash"):
    x=c*(0.1)
    c-=x
else:
    x=c*(0.05)
    c-=x
print(f"cost of ticket : {c}")
