#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// Candidates have name and vote count
typedef struct
{
    string name;
    int votes;
} candidate;

// Array of candidates
candidate candidates[MAX];

// Number of candidates
int candidate_count;

// Function prototypes
bool vote(string name);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: plurality [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
    }

    int voter_count = get_int("Number of voters: ");

    // Loop over all voters
    for (int i = 0; i < voter_count; i++)
    {
        string name = get_string("Vote: ");

        // Check for invalid vote
        if (!vote(name))
        {
            printf("Invalid vote.\n");
        }
    }

    // Display winner of election
    print_winner();
}

// Update vote totals given a new vote
bool vote(string name)
{
    // TODO
    int i = 0;
    // Loop through the candidate quanitity
    while (i < candidate_count)
    {
        // If candidate name exists
        if (strcmp(candidates[i].name, name) == 0)
        {
            // Add 1 vote to him and return
            candidates[i].votes += 1;
            return true;
        }
        // Add 1 to index
        i++;
    }
    // Return false if name is not present on structure
    return false;
}

// Print the winner (or winners) of the election
void print_winner(void)
{
    // TODO
    // Loop to get the instance I of struct
    for (int i = 0; i < candidate_count; i++)
    {
        // Define an auxiliar to store data and change positions if necessary
        candidate aux;
        // Second loop to go through the struct and get all instances to compare with I instance
        for (int y = 0; y < candidate_count; y++)
        {
            // Check if the candidates in Y position has more votes than the I
            if (candidates[y].votes < candidates[i].votes)
            {
                // Save data from candidate Y instance
                aux = candidates[y];
                // Trade candidate Y instance data from candidate in I instance
                candidates[y] = candidates[i];
                // Trade candidate I instance data from candidate in Y that was stored in AUX
                candidates[i] = aux;
            }
        }
    }

    int j = 0;
    // With the structure organized do a loop until candidate quantity
    while (j < candidate_count)
    {
        // Print the first index of candidates that has more votes
        printf("%s\n", candidates[j].name);
        // Compare if the actual index has the same quantity of votes that the next candidate
        // if not just return, else continue loop to print name of next candidate
        if (candidates[j].votes != candidates[j + 1].votes)
        {
            return;
        }
        j++;
    }
    return;
}