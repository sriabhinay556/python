str = input("Enter string : ")
for i in range(len(str)):
    if(str[i] == " "):
        str = str.replace(str[i], '-')
print(str)
