#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int quantitySteps = 0;

    // Repeat until user provide a number between 0 and 9
    do
    {
        quantitySteps = get_int("Height: ");

    }
    while (quantitySteps < 1 || quantitySteps > 8);

    // Do a loop through the quantity steps representing each line
    for (int i = 1; i <=  quantitySteps; i++)
    {
        // Loop to check and print each step from line in staircase that is going up
        for (int y = quantitySteps; y >= 1; y--)
        {
            if (y <= i)
            {
                printf("#");
            }
            else
            {
                printf(" ");
            }
        }

        // Print white space to separate staircase
        printf("  ");

        // Loop to check and print each step from line in staincase that is going down
        for (int y = 1; y <= quantitySteps; y++)
        {
            if (y <= i)
            {
                printf("#");
            }
        }

        // Break the line to continue loop
        printf("\n");
    }

}