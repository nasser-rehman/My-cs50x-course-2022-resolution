#include <cs50.h>
#include <stdio.h>

int get_cents(void);
int calculate_quarters(int cents);
int calculate_dimes(int cents);
int calculate_nickels(int cents);
int calculate_pennies(int cents);

int main(void)
{
    // Ask how many cents the customer is owed
    int cents = get_cents();

    // Calculate the number of quarters to give the customer
    int quarters = calculate_quarters(cents);
    cents = cents - quarters * 25;

    // Calculate the number of dimes to give the customer
    int dimes = calculate_dimes(cents);
    cents = cents - dimes * 10;

    // Calculate the number of nickels to give the customer
    int nickels = calculate_nickels(cents);
    cents = cents - nickels * 5;

    // Calculate the number of pennies to give the customer
    int pennies = calculate_pennies(cents);
    cents = cents - pennies * 1;

    // Sum coins
    int coins = quarters + dimes + nickels + pennies;

    // Print total number of coins to give the customer
    printf("%i\n", coins);
}

int get_cents(void)
{
    // TODO
    int enter_cash = 0;
    // Ask user for input and loop if input is lower or equals 0
    do
    {
        enter_cash = get_int("Change owed: ");
    }
    while (enter_cash <= 0);
    return enter_cash;
}

int calculate_quarters(int cents)
{
    // TODO
    int counter = 0;

    // While cents is greater than 25 (quarters), add one to counter and
    // subtract from cents the value of a quarter
    while (cents >= 25)
    {
        counter++;
        cents = cents - 25;
    }
    return counter;
}

int calculate_dimes(int cents)
{
    // TODO
    int counter = 0;
    // While cents is greater than 10 (dimes), add one to counter and
    // subtract from cents the value of a dime
    while (cents >= 10)
    {
        counter++;
        cents = cents - 10;
    }
    return counter;
}

int calculate_nickels(int cents)
{
    // TODO
    int counter = 0;
    // While cents is greater than 5 (nickels), add one to counter and
    // subtract from cents the value of a nickel
    while (cents >= 5)
    {
        counter++;
        cents = cents - 5;
    }
    return counter;
}

int calculate_pennies(int cents)
{
    // TODO
    int counter = 0;
    // While cents is greater than 1 (pennies), add one to counter and
    // subtract from cents the value of a pennie
    while (cents >= 1)
    {
        counter++;
        cents = cents - 1;
    }
    return counter;
}
