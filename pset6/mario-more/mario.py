import cs50


def main():
    while True:
        height = cs50.get_int("Height: ")
        if height > 0 and height < 9:
            break
    # Do an loop through lines and columns
    for i in range(1, height + 1):
        for j in range(1, height + 1):
            # Imprime # depois do número correto de espaços
            # Prints # after the correct number of spaces
            if j > (height - i):
                print("#", end="")
            else:
                print(" ", end="")

            # Print a space to separate stairs and the # lefts
            if j == height:
                print(" ", "#" * i, end="")
        print("")


main()