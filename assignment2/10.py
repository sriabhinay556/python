inp = input("Enter YYYY-MM-DD : ")
inp = [int(e) for e in inp.split("-")]
if(inp[0] % 4 == 0 or not inp[0] % 100 == 0 or inp[0] % 400 == 0):
    leap = True
else:
    leap = False
if(inp[1] in (1, 3, 5, 7, 8, 10, 12)):
    days = 31
elif(inp[1] == 2):
    if(leap):
        days = 29
    else:
        days = 28
else:
    days = 30
if(not inp[1] == 12):
    if(inp[2] == days):
        inp[2] = 1
        inp[1] += 1
    else:
        inp[2] += 1
else:
    if(inp[2] == days):
        inp[2] = 1
        inp[1] = 1
        inp[0] += 1
print(inp)
