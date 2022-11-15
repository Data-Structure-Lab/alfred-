#include<stdio.h>
int main()
{
int sum=0,num,r;
printf("enter the number");
scanf("%d",&num);
while(num>0)
{
r=num%10;
sum=sum+r;
num=num/10;
}
printf("sum is %d",sum);
return(0);
}
