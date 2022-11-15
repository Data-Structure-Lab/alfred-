list1=[]
n=int(input("enter number of element"))
for i in range(0,n):
  ele = int(input())
  list1.append(ele)
print(list1)
def sumoflist(list,size):
    if(size==0):
        return 0
    else:
        return list[size - 1] + sumoflist(list, size - 1)
total = sumoflist(list1, len(list1))
print("sum of all elements in given list:",total)
