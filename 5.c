#include<stdio.h>
void main()
{
int a,b,c;
printf("enter your number");
scanf("%d%d%d",&a,&b,&c);
if(a>b)
{
printf("%d is greater than %d",a,b);
}
else if (a>c)
{
printf("%d is greater than %d",a,c);
}

else if (b>a)
{
printf("%d is greater than  %d",b,a);
}
else if (b>c)
{
printf("%d is greater than %d",b,c);

}
else if (c>a)
{
printf("%d is greater than %d",c,a);
}
else if (c>b)
{
printf("%d is greater than %d",c,b);
}
}
