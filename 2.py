list=[]
n=int(input("enter a number"))
for i in range(0,n):
    list.append(int(input()))
print(list)
result=[]
for i in list:
    if (i >100):
        result.append('over')
            
    else:
        result.append(i)
print(result)
