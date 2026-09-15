#include<stdio.h>
void print(int i, int n)
{
    for(i=0;i<n;i++)
    {
        printf("hello\n");
    }
}

int main()
{
    int n;
    print(0,3);
    return 0;
}