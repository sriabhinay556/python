year = int(input("Enter year :"))
print((year % 4 == 0 and not year % 100 == 0) or (year % 400 == 0))
