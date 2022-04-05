#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int initial;
    int final;
    int years = 0;

    // Get initial size
    do
    {
        initial = get_int("Start size: ");
    }
    while (initial < 9);

    // Get final size
    do
    {
        final = get_int("End size: ");
    }
    while (final < initial);

    // Count quantity of years
    while (initial < final)
    {
        int birth, dead;
        birth = initial / 3;
        dead = initial / 4;
        initial = initial + birth;
        initial = initial - dead;
        years++;
    }

    printf("Years: %i\n", years);

}