import cs50
import string


def main():
    # Get input from user
    text = cs50.get_string("Text: ")
    # Initialize variables that is gonna be used by counters
    letters = 0
    words = 1
    sentences = 0

    # Loop through all string provided by user
    for index in text:
        # Check if index is a type of '!, . or ?' punctuation assuming that is a final of phrase
        if index == '!' or index == '.' or index == '?':
            # Add 1 to sentences counter if true
            sentences += 1
        # If it is another type of punctuation just continue loop
        elif index in string.punctuation:
            continue
        # Check if index is a white space assuming that is a final of word
        elif index in string.whitespace:
            # Add 1 to words counter
            words += 1
        # Else add 1 to letters counters
        else:
            letters += 1

    # Calculates the average number of words by 100
    factorWord = words / 100
    # Calculates the average of Letter by average of Words
    factorLetters = letters / factorWord
    # Calculates the average of Sentences by average of words
    factorSentences = sentences / factorWord

    # Calculates the grade according to Coleman-Liau index
    grade = round((0.0588 * factorLetters) - (0.296 * factorSentences) - 15.8)

    # Check conditions and print the grade of text provided by user
    if grade < 16 and grade >= 0:
        print(f"Grade {round(grade)}")
    elif grade > 16:
        print("Grade 16+")
    else:
        print("Before Grade 1")


main()