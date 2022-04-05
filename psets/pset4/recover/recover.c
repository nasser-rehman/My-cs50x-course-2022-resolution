#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main(int argc, char *argv[])
{
    // If arguments is invalid return message
    if (argc != 2)
    {
        printf("Usage: ./recover card.raw");
        return 1;
    }
    // Open file raw
    FILE *input_file = fopen(argv[1], "r");

    // Check pointer of file
    if (input_file == NULL)
    {
        printf("Could not open file");
        return 2;
    }

    // Initialize variables
    unsigned char buffer[512];
    int count = 0;
    FILE *output_file = NULL;
    char *filename = malloc(8 * sizeof(char));

    // Repeat until the end of card
    while (fread(buffer, sizeof(char), 512, input_file))
    {
        // Verify if the start of header file is a JPEG (0xff 0xd8 0xff 0xe0)
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // Initialize ile
            sprintf(filename, "%03i.jpg", count);

            // open output file to write
            output_file = fopen(filename, "w");
            // Count the quantity of image +1
            count++;
        }

        // Verify if output file is valid
        if (output_file != NULL)
        {
            // Write JPEG to file
            fwrite(buffer, sizeof(char), 512, output_file);
        }

    }
    // Free pointer and close files
    free(filename);
    fclose(output_file);
    fclose(input_file);

    return 0;
}