list1=[]
list2=[]
n=int(input("enter the elements"))
for i in range(0,n):
    list1.append(int(input()))
print("FIRST LIST IS: ",list1)
num=int(input("enter the element"))
for i in range(0,num):
    list2.append(int(input()))
    print("first list is : ",list2)
    len1=len(list1)
    len2=len(list2)
    if len1==len2:
        print("two list are same length")

    else:
            print("length are not same")
s=0
for i in list1:
    s=s+i
    print(s)
t=0
for i in list2:
    t=t+i
    print(t)
if s==t:
        
        print("sum are same ")
else:
        print("sum are not same")


        
z=int(input("enter a number"))
if z in list1 and list2:
        print(z)
else:
        print("no elements are common")
common=set(list1).intersection(list2)
print(common,"occur in both")
    

              


        
    
    
