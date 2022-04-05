#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

bool checkhash(long card_number);

int main(void)
{
    // Get input from user
    long n = get_long("Number: ");

    // Used to count the length of long
    int counter = 0;

    // Auxiliar to operate division without lost the original input
    long n_aux = n;

    // Iterate into long value to get the length value of input
    while (n_aux != 0)
    {
        n_aux /= 10;
        counter++;
    }

    // Checks if the length is valid
    if (counter != 13 && counter != 15 && counter != 16)
    {
        printf("INVALID\n");
        return 0;
    }

    if (!checkhash(n))
    {
        printf("INVALID\n");
        return 0;
    }

    // Auxiliar to operate division without lost the original input
    long first_second_digit = n;

    // Iterate into long value to reach the first two characters
    do
    {
        first_second_digit /= 10;
    }
    while (first_second_digit > 100);
    // Get first digit
    long first = first_second_digit / 10;
    // Get second digit
    long second = first_second_digit % 10;

    // Check conditions to print the correct card
    if (first == 5 && second >= 1 && second <= 5)
    {
        printf("MASTERCARD\n");
    }
    else if (first == 4)
    {
        printf("VISA\n");
    }
    else if ((first == 3) && (second == 4 || second == 7))
    {
        printf("AMEX\n");
    }
    else
    {
        printf("INVALID\n");
    }
}

// Check if the card number is valid according to Luhn Algorithm
bool checkhash(long cardnumber)
{
    int sum = 0;
    int i = 0;
    do
    {
        if (i % 2 != 0)
        {
            int aux = 2 * (cardnumber % 10);
            sum += aux / 10 + aux % 10;
        }
        else
        {
            sum += cardnumber % 10;
        }
        i++;
        cardnumber /= 10;
    }
    while (cardnumber != 0);
    return (sum % 10) == 0;
}