#include <stdio.h>

int fact(int n)
{
    if (n < 0)
    {
        return -1;
    }
    
    if (n == 0)
    {
        return 1;
    }
    
    return n * fact(n - 1);
}

int main()
{
    int n;

    printf("Enter the n: ");
    scanf("%d", &n);

    if (n < 0)
    {
        printf("Factorial is not defined for negative numbers.");
    }
    else
    {
        printf("fact = %d", fact(n));
    }

    return 0;
}