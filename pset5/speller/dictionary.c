// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

unsigned int size_of_dictionary = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    char temp[LENGTH + 1] = {'\0'};

    // Copý the word passed to function
    for (int i = 0; word[i]; i++)
    {
        temp[i] = word[i];
    }

    // Pass the world to lower case
    for (int i = 0; temp[i]; i++)
    {
        temp[i] = tolower(temp[i]);
    }

    // Hash the word to number
    int pos = hash(temp);

    // Create a pointer to the position in hashtable
    node *pointer = table[pos];


    while (true)
    {
        // Iterates through all letter of the word
        for (int i = 0; i <= LENGTH; i++)
        {
            // Compares character by character
            if (pointer->word[i] != temp[i])
            {
                break;
            }

            // If all the character in array is equals
            if (i == LENGTH)
            {
                return true;
            }
        }

        if (!pointer->next)
        {
            // Can't find the word in dictionarie
            return false;
        }
        // Set pointer to next address
        pointer = pointer->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    return tolower(word[0]) - 'a';
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    int i = 0;
    // Initialize hash table
    while (i < N)
    {
        table[i] = NULL;
        i++;
    }

    // Try open file
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        unload();
        return false;
    }

    // Buffer for one word
    char word[LENGTH + 1];

    // Insert words into table hash
    while (fscanf(file, "%s", word) != EOF)
    {
        // Add 1 to dictionary size
        size_of_dictionary++;

        // Get the position of word
        int pos = hash(word);

        // Allocate memory to the new word
        node *n_word = malloc(sizeof(node));
        memset(n_word->word, '\0', sizeof(word));

        // Insert the words in hash table
        if (table[pos])
        {
            // Pass the word from buffer to node
            for (int y = 0; word[y]; y++)
            {
                n_word->word[y] = word[y];
            }

            // Insert node into linked list
            n_word->next = table[pos];
            table[pos] = n_word;
        }
        else
        {
            table[pos] = n_word;

            for (int y = 0; word[y]; y++)
            {
                n_word->word[y] = word[y];
            }

            n_word->next = NULL;
        }
    }
    printf("Loaded %u words\n", size_of_dictionary);
    // Close dictionary
    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return size_of_dictionary;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    int i = 0;
    while (i < N)
    {
        node *pointer = table[i];

        while (pointer)
        {
            node *temp = pointer;
            pointer = pointer->next;
            free(temp);
        }
        i++;
    }
    return true;
}
