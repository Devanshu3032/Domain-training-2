n = input("enter a number : ")
res = [] 
for i in range(1,6) :
    if(i%3 == 0 and i %5 == 0 ):
        res.append("fizzBuzz")
    elif(i%3 == 0 ):
        res.append("fizz") 
    elif(i % 5 == 0) :
        res.append("Buzz")
    else :
        res.append(str(i))
        
print(res)