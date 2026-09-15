#include<stdio.h>
int revarr(int arr[100] ,int n)
{
    int b[100],i;
    for(i=n-1;i>=0;i--)
    {
        b[n-i-1] = arr[i];
    }
    return b;
}

int main()
{
    int arr[100],n,i;
    printf("Enter the size of array: ");
    scanf("%d",&n);
    printf("Enter the elements of array: ");
    for(i=0;i<n;i++)
    {
        scanf("%d",&arr[i]);
    }
    int *rev = revarr(arr,n);
    printf("Reversed array: ");
    for(i=0;i<n;i++)
    {
        printf("%d ",rev[i]);
    }
    return 0;
}