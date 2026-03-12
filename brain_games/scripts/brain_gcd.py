from brain_games import games, launcher


def main():
    print('Welcome to the Brain Games!')
    launcher.launch_game(games.gcd)


if __name__ == "__main__":
    main()
