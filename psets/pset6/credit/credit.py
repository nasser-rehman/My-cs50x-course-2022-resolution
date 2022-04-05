import cs50


def main():
    # Ask user to Credit Card Number
    cn = cs50.get_string("CREDIT CARD NUMBER: ")

    # Check if length of string provided is valid
    if len(cn) < 13 or len(cn) > 16:
        print("INVALID")
        return
    cn_aux = ""

    # Invert string
    for aux_char in cn[:: -1]:
        cn_aux = cn_aux + aux_char

    # Check Luhn's Algorithm
    if int(check_validity(cn_aux)) != 0:
        print("INVALID")
        return

    # Call get two first digits
    first_two_digits = get_two_first_digits(cn)

    # Check conditions and print the card flag
    if int(first_two_digits) == 34 or int(first_two_digits) == 37:
        print("AMEX")
    elif int(first_two_digits) >= 51 and int(first_two_digits) <= 55:
        print("MASTERCARD")
    elif int(first_two_digits) >= 40 and int(first_two_digits) <= 49:
        print("VISA")
    else:
        print("INVALID")

    return


# Check Card Number
def check_validity(cn):
    count = 0
    # Loop through entire card number incrementing by 2 initialing from second position of string array
    for char_index in cn[1: len(cn): 2]:
        # Get char in position and multiply by 2
        char_retired = str(int(char_index)*2)
        # If value is higher than 9 so needed to be separated and added
        if(int(char_retired) > 9):
            # Loop through multiplied value and get single integer to added on count
            for char_sub in range(len(char_retired)):
                count = count + int(char_retired[char_sub])
        # If value is lower than 9 than just add value to count
        else:
            count = count + int(char_retired)

    # Loop through entire card number incrementing by 2 initialing from first position of string array
    for char_index in cn[0: len(cn): 2]:
        # Added on count
        count = count + int(char_index)

    # Return value mod 10 accourding Luhn's Algorithm
    return count % 10


# Get the first decimal digits
def get_two_first_digits(cn):
    digits = ""
    # Loop through 2 first digits of credit card number
    for char_index in cn[0: 2: 1]:
        digits = digits + char_index

    return digits


main()