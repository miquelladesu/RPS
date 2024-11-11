#!/usr/bin/env python3

import random
import os
import sys
from time import sleep

# ANSI color codes because its nice lol
COLORS = {
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'purple': '\033[95m',
    'cyan': '\033[96m',
    'reset': '\033[0m'
}

# Game symbols
SYMBOLS = {
    'rock': '🪨',
    'paper': '📄',
    'scissors': '✂️'
}

class RockPaperScissors:
    def __init__(self):
        """Initialize the game with score tracking."""
        self.scores = {'player': 0, 'computer': 0}
        self.choices = ['rock', 'paper', 'scissors']

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_title(self):
        title = """
╔═══════════════════════════════════════════╗
║           ROCK PAPER SCISSORS             ║
║       Battle Against Computer-chan        ║
╚═══════════════════════════════════════════╝
"""
        print(f"{COLORS['cyan']}{title}{COLORS['reset']}")

    def print_scores(self):
        print(f"\n{COLORS['yellow']}═══ SCORE BOARD ═══{COLORS['reset']}")
        print(f"🎮 Player: {COLORS['green']}{self.scores['player']}{COLORS['reset']}")
        print(f"🤖 Computer-chan: {COLORS['red']}{self.scores['computer']}{COLORS['reset']}\n")

    def get_computer_choice(self) -> str:
        """Return a random choice for the computer."""
        return random.choice(self.choices)

    def get_user_choice(self) -> str:
        """Get and validate user input for their choice."""
        while True:
            self.clear_screen()
            self.print_title()
            self.print_scores()
            print(f"Choose your weapon:")
            for i, choice in enumerate(self.choices, 1):
                print(f"{i}. {choice.title()} {SYMBOLS[choice]}")
            try:
                choice = input("\nEnter your choice (1-3): ").strip()
                if choice in ['1', '2', '3']:
                    return self.choices[int(choice) - 1]
                print(f"{COLORS['red']}Invalid choice! Please enter 1, 2, or 3.{COLORS['reset']}")
                sleep(1)
            except KeyboardInterrupt:
                print("\nThanks for playing! Goodbye! 👋")
                sys.exit(0)

    def determine_winner(self, user_choice: str, computer_choice: str) -> str:
        """Determine the winner based on the choices made."""
        if user_choice == computer_choice:
            return 'tie'
        winning_combos = {
            'rock': 'scissors',
            'paper': 'rock',
            'scissors': 'paper'
        }
        return 'player' if winning_combos[user_choice] == computer_choice else 'computer'

    def display_round_result(self, user_choice, computer_choice, winner):
        print(f"\n{'═' * 40}")
        print(f"Your choice: {COLORS['green']}{user_choice.title()} {SYMBOLS[user_choice]}{COLORS['reset']}")
        print(f"Computer-chan's choice: {COLORS['red']}{computer_choice.title()} {SYMBOLS[computer_choice]}{COLORS['reset']}")
        print(f"{'═' * 40}\n")

        if winner == 'tie':
            print(f"{COLORS['yellow']}🎯 It's a tie!{COLORS['reset']}")
        elif winner == 'player':
            print(f"{COLORS['green']}🎉 You win!{COLORS['reset']}")
            self.scores['player'] += 1
        else:
            print(f"{COLORS['red']}💔 Computer-chan wins!{COLORS['reset']}")
            self.scores['computer'] += 1

    def play(self):
        while True:
            user_choice = self.get_user_choice()
            computer_choice = self.get_computer_choice()
            winner = self.determine_winner(user_choice, computer_choice)

            self.clear_screen()
            self.print_title()
            self.display_round_result(user_choice, computer_choice, winner)

            try:
                again = input(f"\nPlay again? (y/n): ").lower().strip()
                if again != 'y':
                    print(f"\n{COLORS['cyan']}Final Scores:{COLORS['reset']}")
                    self.print_scores()
                    print(f"\nThanks for playing! Goodbye! 👋")
                    break
            except KeyboardInterrupt:
                print("\nThanks for playing! Goodbye! 👋")
                break

if __name__ == "__main__":
    try:
        game = RockPaperScissors()
        game.play()
    except KeyboardInterrupt:
        print("\nThanks for playing! Goodbye! 👋")
