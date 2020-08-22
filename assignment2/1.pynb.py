a = float(input("Enter side a :"))
b = float(input("Enter side b :"))
c = float(input("Enter side c :"))
p = float((a+b+c))*0.5
print((p*(p - a)*(p - b)*(p - c)) ** (0.5))
