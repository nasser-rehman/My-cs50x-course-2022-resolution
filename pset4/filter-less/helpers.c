#include "helpers.h"
#include "math.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    int i = 0;

    // Iterate through all columns of pixels
    while (i < height)
    {
        int j = 0;
        // Iterate through all rows of pixels
        while (j < width)
        {
            // Get all value of each color and calculate the average of each pixel
            int average = round(((float)image[i][j].rgbtRed + (float)image[i][j].rgbtGreen + (float)image[i][j].rgbtBlue) / 3);

            // Set the average to the new value of each pixel
            image[i][j].rgbtRed = average;
            image[i][j].rgbtGreen = average;
            image[i][j].rgbtBlue = average;
            j++;
        }
        i++;
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    int i = 0;
    while (i < height)
    {
        int j = 0;
        while (j < width)
        {
            // Store original values
            int o_red = image[i][j].rgbtRed;
            int o_green = image[i][j].rgbtGreen;
            int o_blue = image[i][j].rgbtBlue;

            // Calculate sepia red
            int s_red = round(0.393 * o_red + 0.769 * o_green + 0.189 * o_blue);
            // Calculate sepia green
            int s_green = round(0.349 * o_red + 0.686 * o_green + 0.168 * o_blue);
            // Calculate sepia blue
            int s_blue = round(0.272 * o_red + 0.534 * o_green + 0.131 * o_blue);

            if (s_red > 255)
            {
                image[i][j].rgbtRed = 255;
            }
            else
            {
                image[i][j].rgbtRed = s_red;
            }

            if (s_green > 255)
            {
                image[i][j].rgbtGreen = 255;
            }
            else
            {
                image[i][j].rgbtGreen = s_green;
            }

            if (s_blue > 255)
            {
                image[i][j].rgbtBlue = 255;
            }
            else
            {
                image[i][j].rgbtBlue = s_blue;
            }

            j++;
        }
        i++;
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    int i = 0;
    while (i < height)
    {
        // Iterate until get into to the middle of 'image'
        for (int j = 0; j < (width / 2); j++)
        {
            // Swap pixels
            RGBTRIPLE aux = image[i][j];
            image[i][j] = image[i][width - (j + 1)];
            image[i][width - (j + 1)] = aux;
        }
        i++;
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // Temp image to manipulate data
    RGBTRIPLE temp_image[height][width];

    int i = 0;
    while (i < height)
    {
        int j = 0;
        while (j < width)
        {
            int total_red = 0;
            int total_green = 0;
            int total_blue = 0;
            float counter = 0;

            // Get neighboring pixels
            for (int x = -1; x < 2; x++)
            {
                for (int y = -1; y < 2; y++)
                {
                    int current_x = x + i;
                    int current_y = y + j;

                    // Check the validity of neighboring pixels
                    if (current_x < 0 || current_x > (height - 1) || current_y < 0 || current_y > (width - 1))
                    {
                        continue;
                    }

                    total_red += image[current_x][current_y].rgbtRed;
                    total_green += image[current_x][current_y].rgbtGreen;
                    total_blue += image[current_x][current_y].rgbtBlue;
                    counter++;
                }

                // Do average on neighboring pixels
                temp_image[i][j].rgbtRed = round(total_red / counter);
                temp_image[i][j].rgbtGreen = round(total_green / counter);
                temp_image[i][j].rgbtBlue = round(total_blue / counter);
            }

            j++;
        }
        i++;
    }

    i = 0;
    // Copie image with blur stored in temp_image to the original one
    while (i < height)
    {
        int j = 0;
        while (j < width)
        {
            image[i][j].rgbtRed = temp_image[i][j].rgbtRed;
            image[i][j].rgbtGreen = temp_image[i][j].rgbtGreen;
            image[i][j].rgbtBlue = temp_image[i][j].rgbtBlue;
            j++;
        }
        i++;
    }

    return;
}
