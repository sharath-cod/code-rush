#include<stdio.h>
int print(int i, int n)
{
    int count = 0;

    for (i=0;i<n;i++)
    {
        count+=i;
        printf("the sum of 1st %d  number is %d\n",n,count);
    }
    return 0;
}

int main()
{
    int n;
    printf("enter the number:");
    scanf("%d",&n);
    print(0,n);
    return 0;
}