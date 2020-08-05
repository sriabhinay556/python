month=input()
print("Season :",end="")
if(month.lower()=="december" or month.lower()=="january" or month.lower()=="february"):
    print("Winter")
elif(month.lower()=="march" or month.lower()=="april" or month.lower()=="may"):
    print("Spring")
elif(month.lower()=="june" or month.lower()=="july" or month.lower()=="august"):
    print("summer")
else:
    print("Autumn")
