import cs50


def main():
    enter_cash = 0

    # Loop while user input is lower than 1
    while True:
        enter_cash = cs50.get_float("Change owed: ")

        if enter_cash > 0:
            break

    counter_change = 0

    # Round cash value to work with decimals
    enter_cash = round(enter_cash * 100)

    # Loop while input provided by user is higher or equals 25
    while enter_cash >= 25:
        # Add 1 to money change counter
        counter_change += 1
        # Subtract value 25 of cash provided by user
        enter_cash = enter_cash - 25

    # Loop while input provided by user is higher or equals 25
    while enter_cash >= 10:
        # Add 1 to money change counter
        counter_change += 1
        # Subtract value 10 of cash provided by user
        enter_cash = enter_cash - 10

    # Loop while input provided by user is higher or equals 5
    while enter_cash >= 5:
        # Add 1 to money change counter
        counter_change += 1
        # Subtract value 5 of cash provided by user
        enter_cash = enter_cash - 5

    # Loop while input provided by user is higher or equals 1
    while enter_cash >= 1:
        # Add 1 to money change counter
        counter_change += 1
        # Subtract value 1 of cash provided by user
        enter_cash = enter_cash - 1

    # Print the money change quantity
    print(counter_change)


main()