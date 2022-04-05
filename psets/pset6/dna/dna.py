import cs50
import csv
from sys import argv


def main(argv):
    search_patterns = {}
    pattern = ""
    result = {}
    result_name = ""

    # Check if user provided args correctly
    if(len(argv) != 3):
        # If not print usage
        print("Usage: python dna.py data.csv sequence.txt")
    else:
        # Open file
        with open(argv[1], "r") as file:
            # Read file like Dictionary
            reader = csv.DictReader(file)
            # Convert dictionary to list
            dict_csv = dict(list(reader)[0])
            # Get list of patterns
            list_names = list(dict_csv.keys())
            # Loop through list of patterns and save into variable
            for row in list_names[1: len(list_names): 1]:
                search_patterns[row] = 0

        # Open file of sequences and read the string to variable
        with open(argv[2], "r") as file_txt:
            pattern = file_txt.read()

    # Loop through entire list of patterns and assign the quantity of each pattern on each key
    for key, value in search_patterns.items():
        search_patterns[key] = findQuantity(pattern, key)

    # Open database again
    with open(argv[1], "r") as file:
        # Read as dict
        reader = csv.DictReader(file)

        for line in reader:
            name = ""
            # Loop through each line of database
            for key, value in line.items():
                # If key equals name
                if key == "name":
                    # Save name of people
                    result_name = value
                # Else some pattern
                elif key != "name":
                    # Check if the value of database is equals of counter present in search_patterns of this people
                    if (int(value) == int(search_patterns[key])):
                        # If yes set flag to result
                        result[key] = int(1)
                    else:
                        # else not
                        result[key] = int(0)

            # Checks if there is an array with all flags at 1
            # if exists function all return TRUE else false
            res = all(x == 1 for x in result.values())

            if res == True:
                # Print result name stored
                print(result_name)
                return

        if res == False:
            print('No match')
            return


# Count quantity of each pattern
def findQuantity(pattern, key):
    # Gets the total quantity of pattern
    count = pattern.count(key)
    # If pattern is not presented in pattern return
    if count == 0:
        return 0
    # Loop in range of count until 0
    for i in range(count, 0, -1):
        # Try to find in string pattern the quantity of repetitions multiplying
        # the i index and the key
        if key*i in pattern:
            # Returns the index that contains the maximum number of repetitions found by key
            return i


main(argv)