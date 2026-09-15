#include<stdio.h>
int print(int i, int n)
{
    for (i=0;i<n;i++)
    {
        printf("%d\n",n);
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
