#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

// Define an string with original ordenation of alphabet
string alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
// Define functions prototypes
bool check_if_character(string key);
string transform_to_upper(string key);
bool check_character_repetition(string key);
void encrypt_text(string key, string text);

int main(int argc, string argv[])
{
    // Check if user provided key
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }

    // Store key to variable
    string key = argv[1];

    // Check if key is length of 26 and if all is characters and if not have duplications
    if (strlen(key) != 26 || !check_if_character(key) || !check_character_repetition(key))
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }

    // Transform all characters to uppercase
    key = transform_to_upper(key);

    // Get text to encrypt
    string text = get_string("plaintext: ");

    // Encrypt and print the encrypted text;
    encrypt_text(key, text);
}

// Encrypt and print the text
void encrypt_text(string key, string text)
{
    printf("ciphertext: ");
    // Loop through the entire string
    for (int i = 0; i < strlen(text); i++)
    {
        // Check if char of string is not a space, digit or punctuation, if it is print without encrypt
        if (!isspace(text[i]) && !isdigit(text[i]) && !ispunct(text[i]))
        {
            // Loop through the entire alphabet
            for (int y = 0; y < strlen(alphabet); y++)
            {
                // Check if character is lower case to compare with alphabet that is uppercase
                if (islower(text[i]))
                {
                    // If is lower, transform to uppercase and gets the position of alphabet
                    if (toupper(text[i]) == alphabet[y])
                    {
                        // Print encrypted char with position in key
                        printf("%c", tolower(key[y]));
                    }
                }
                // If is not uppercase just print char with position of y in key
                else
                {
                    if (text[i] == alphabet[y])
                    {
                        printf("%c", key[y]);
                    }
                }
            }
        }
        // If is space, digit or punctuation just print
        else
        {
            printf("%c", text[i]);
        }
    }
    printf("\n");
}

// Check if key is all characters
bool check_if_character(string key)
{
    // Loop through entire key
    for (int i = 0; i < strlen(key); i++)
    {
        // If not alphabetic return false
        if (!isalpha(key[i]))
        {
            return false;
        }
    }
    return true;
}

// Transform all key character to uppercase
string transform_to_upper(string key)
{
    // Loop through entire key
    for (int i = 0; i < strlen(key); i++)
    {
        // Transform to upper
        key[i] = toupper(key[i]);
    }

    // return new key in uppercase
    return key;
}

// Check if in key have duplicated chars
bool check_character_repetition(string key)
{

    // Transform all key in uppercase
    key = transform_to_upper(key);

    // Loop through entire key to get the i instance
    for (int i = 0; i < strlen(key); i++)
    {
        // Loop through entire key to get the y instance
        for (int y = 0; y < strlen(key); y++)
        {
            // Compare if i and y is the same istance to not check if is duplicated
            if (i != y)
            {
                // If key have the same char return false
                if (key[i] == key[y])
                {
                    return false;
                }
            }
        }
    }

    // If not have duplicated chars
    return true;
}