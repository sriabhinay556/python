num = input("Enter 3 numbers with commas in btw : ")
num = [int(e) for e in num.split(",")]
print(min(num), (num[0]+num[1]+num[2])-(max(num)+min(num)), max(num))
