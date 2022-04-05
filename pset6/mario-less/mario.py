import cs50


def main():
    while True:
        height = cs50.get_int("Height: ")
        if height > 0 and height < 9:
            break

    for i in range(1, height + 1):
        for j in range(1, height + 1):
            if j > (height - i):
                print("#", end="")
            else:
                print(" ", end="")
        print("")


main()