# Simulate a sports tournament

import csv
import sys
import random

# Number of simluations to run
N = 1000


def main():

    # Ensure correct usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python tournament.py FILENAME")

    teams = []
    # TODO: Read teams into memory from file
    filename = sys.argv[1]
    # Open file
    with open(filename, 'r') as file:
        # Read file like Dictionary
        reader = csv.DictReader(file)
        # Loop for each line in reader
        for line in reader:
            aux_team = {}
            # Loop through each key and value of line
            for key, value in line.items():
                # If key is team
                if key == "team":
                    # Save name of team
                    aux_team[key] = value
                else:
                    # Save rating value
                    aux_team[key] = int(value)
            # Add team to teams array
            teams.append(aux_team)

    counts = {}
    # TODO: Simulate N tournaments and keep track of win counts
    for i in range(N):
        # Store winner of tournament
        winner = simulate_tournament(teams)
        # Check if winner is already present in counts array
        if winner in counts:
            # If yes plus 1
            counts[winner] += 1
        else:
            # Else just assign 1
            counts[winner] = 1

    # Print each team's chances of winning, according to simulation
    for team in sorted(counts, key=lambda team: counts[team], reverse=True):
        print(f"{team}: {counts[team] * 100 / N:.1f}% chance of winning")


def simulate_game(team1, team2):
    """Simulate a game. Return True if team1 wins, False otherwise."""
    rating1 = team1["rating"]
    rating2 = team2["rating"]
    probability = 1 / (1 + 10 ** ((rating2 - rating1) / 600))
    return random.random() < probability


def simulate_round(teams):
    """Simulate a round. Return a list of winning teams."""
    winners = []

    # Simulate games for all pairs of teams
    for i in range(0, len(teams), 2):
        if simulate_game(teams[i], teams[i + 1]):
            winners.append(teams[i])
        else:
            winners.append(teams[i + 1])

    return winners


def simulate_tournament(teams):
    """Simulate a tournament. Return name of winning team."""
    # TODO
    # While length of teams is higher than 1 simulate rounds with teams
    while len(teams) > 1:
        teams = simulate_round(teams)
    # Return the winner team
    return teams[0]["team"]


if __name__ == "__main__":
    main()
