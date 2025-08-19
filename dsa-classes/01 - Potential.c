#include <stdio.h>

int exponential(int x, int n)
{
    if (n == 0)
    {
        return 1;
    }
    else if (n == 1)
    {
        return x;
    }

    return x * exponential(x, n - 1);
}

int main()
{

    int result = exponential(2, 3);
    printf("2^3 = %d\n", result);

    return 0;
}