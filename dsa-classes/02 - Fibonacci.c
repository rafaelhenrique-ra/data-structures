// implement fibonacci with recursion
#include <stdio.h>

int fibonacci(int n)
{
    if (n == 0)
    {
        return 0;
    }
    else if (n == 1)
    {
        return 1;
    }

    return fibonacci(n - 1) + fibonacci(n - 2);
}

int main()
{

    printf("Fibonacci sequence:\n");
    for (int i = 0; i <= 5; i++)
    {
        printf("F(%d) = %d\n", i, fibonacci(i));
    }

    return 0;
}