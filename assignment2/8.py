inp = input("Enter Date,Hour,Min,Sec separated btw commas: ")
inp = [int(e) for e in inp.split(",")]
print("No. of seconds", inp[0]*24*60*60+inp[1]*60*60+inp[2]*60+inp[3])
