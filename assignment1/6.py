weight=float(input("Enter the weight:"))
height=float(input("Enter the height:"))
s=weight/(height**2)
if s<18.5:
  print("Underweight")
elif s>=18.5 and s<25.0:
  print("normal")
elif s>=25.0 and s<30.0:
  print("Overweight")
else:
  print("Obese") 
print("BMI is:",s)
