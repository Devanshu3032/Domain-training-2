import random 
res = [] 
while(len(res )!= 5):
    n = random.randint(1, 100)
    if n not in res:
        res.append(n)
print(res)