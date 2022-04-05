#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

bool check_argv_key(char number[]);

int main(int argc, string argv[])
{
    // Check if program usage is correct
    if (argc != 2 || !check_argv_key(argv[1]))
    {
        printf("Usage: ./ceasar k\n");
        return 1;
    }

    // Convert the key provided by user to an integer
    int key = atoi(argv[1]);

    // Ask the text to user
    string text = get_string("plaintext: ");
    // To handle every char on string
    char column;

    // Iterates over the text provided by user
    for (int i = 0; text[i] != '\0'; ++i)
    {
        column = text[i];
        // Check if the value is lowercase
        if (column >= 'A' && column <= 'Z')
        {
            column = column - 'A';
            column += key;
            column = column % 26;
            text[i] = column + 'A';
        }
        // Check if the value if uppercase
        else if (column >= 'a' && column <= 'z')
        {
            column = column - 'a';
            column += key;
            column = column % 26;
            text[i] = column + 'a';
        }
    }

    // Print the ciphertext
    printf("ciphertext: %s\n", text);
    return 0;
}

bool check_argv_key(char number[])
{
    if (number[0] == '-')
    {
        return false;
    }

    for (int i = 0; number[i] != 0; i++)
    {
        if (!isdigit(number[i]))
        {
            return false;
        }
    }
    return true;
}