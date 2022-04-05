#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

int count_letters(string input);
int count_words(string input);
int count_sentences(string input);

int main(void)
{
    // Initialize variables
    string input = get_string("Text: ");
    int letters = count_letters(input);
    int words = count_words(input);
    int sentences = count_sentences(input);

    // Calculate the value of L with the quantity of letters and words
    float L = 100 * (float) letters / (float) words;
    // Calculate the value of S with the quantity of sentences and words
    float S = 100 * (float) sentences / (float) words;

    // Calculates with the grade with Coleman-Liau formula
    float grade = 0.0588 * L - 0.296 * S - 15.8;

    // Check the grade and print it
    if (grade >= 16)
    {
        printf("Grade 16+\n");
    }
    else if (grade < 16 && grade >= 0)
    {
        printf("Grade %i\n", (int)round(grade));
    }
    else
    {
        printf("Before Grade 1\n");
    }
}

// Receive the input from user and return the quantity of letters in it
int count_letters(string input)
{
    int i = 0;
    int letters = 0;
    // Loop while i is lower than length of input
    while (i < strlen(input))
    {
        // Check if the caracter in input at position i is alphabetical
        if (isalpha(input[i]))
        {
            // Add 1 to letters counter
            letters++;
        }
        i++;
    }

    // Return quantity of letters
    return letters;
}

// Receive the input from user and return the quantity of words in it
int count_words(string input)
{
    int i = 0;
    // Declare variable with value 1 initialized to offset last word
    int words = 1;
    // Loop while i is lower than length of input
    while (i < strlen(input))
    {
        // Check if the caracter in input at position i is a space
        if (isspace(input[i]))
        {
            // Add 1 to words counter
            words++;
        }
        i++;
    }

    // Return the quantity of words
    return words;
}

// Receive the input from user and return the quantity of sentences in it
int count_sentences(string input)
{
    int i = 0;
    int sentences = 0;
    // Loop while i is lower than length of input
    while (i < strlen(input))
    {
        // Check if the caracter in input at position i is a dot, an exclamation mark or a question mark
        if (input[i] == '.' || input[i] == '!' || input[i] == '?')
        {
            // Add 1 to sentences counter
            sentences++;
        }
        i++;
    }
    return sentences;
}