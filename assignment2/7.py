inp = input("Enter numbers a comma between : ")
inp = [e for e in inp.split(",")]
s = ""
for e in inp:
    s = s+e
print(int(s))
