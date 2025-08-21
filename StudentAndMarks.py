Student = ['DEVANSHU','RAM','SHYAM','AALOK','MAX']
Marks = [[89,92,87,76,81],[84,78,79,76,73],[89,78,98,56,43],[78,88,90,90,78],[76,98,32,45,67]]
res = []
for i in Marks :
    b = (500-Marks[i]) // 5 
    res.append(b)
    
for i in range(5) : 
    print("{} {} : {} %".format( i+1 , Student, res[i]) )