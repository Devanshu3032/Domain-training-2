a = input("enter a string : ")
b = ""
c = 1 
for i in range(len(a)):
    if(i +1 < len(a) and a[i] == a[i+1]):
        c += 1 
    else: 
        b = b+a[i]
        b = b+str(c)
        c= 1
print(b)    