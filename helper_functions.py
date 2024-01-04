import pathlib
import random
from rich.console import Console
from string import ascii_letters,ascii_uppercase
console = Console(width=40)
def get_random_word():
    wordlist=pathlib.Path("wordlist.txt")
    words=[word.upper() for word in wordlist.read_text(encoding="utf-8").split("\n") if len(word)==5 and all(letter in ascii_letters for letter in word)]
    return random.choice(words)

def show_guesses(guesses,word):
    letter_status={letter:letter for letter in ascii_uppercase}
    for guess in guesses:
        styled_guess=[] 
        for letter,correct in zip(guess,word):
            if letter==correct:
                style="bold white on green"
            elif letter in word:
                style="bold white on yellow"
            elif letter in ascii_letters:
                style="white on #666666"
            else:
                style="dim"
            styled_guess.append(f"[{style}]{letter}[/]")
            if letter !="_":
                letter_status[letter]=f"[{style}]{letter}[/]"
        console.print("".join(styled_guess),justify="center")
    console.print("\n" + "".join(letter_status.values()), justify="center")

def game_over(guesses,word, guessed_correctly):
    refresh_page(headline="End of Game")
    show_guesses(guesses,word)
    if guessed_correctly:
        console.print(f"\n[bold green on white]Correct, the word is {word}[/]")
    else:
        console.print(f"\n[bold red on white]Incorrect, the word was {word}[/]")

def refresh_page(headline):
    console.clear()
    console.rule(f"[bold blue]:green_book: {headline} :green_book:")