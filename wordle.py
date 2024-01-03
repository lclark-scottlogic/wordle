import pathlib
import random
# import nltk
# nltk.download('words')
from nltk.corpus import words
from rich.console import Console
from string import ascii_letters
console = Console(width=40)
def get_random_word():
    wordlist=pathlib.Path("wordlist.txt")
    words=[word.upper() for word in wordlist.read_text(encoding="utf-8").split("\n") if len(word)==5 and all(letter in ascii_letters for letter in word)]
    return random.choice(words)

def show_guesses(guesses,word):
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
        console.print("".join(styled_guess),justify="center")

def game_over(word):
    print(f"The word was {word}")

def refresh_page(headline):
    console.clear()
    console.rule(f"[bold blue]:green_book: {headline} :green_book:")
def main():
    english_words = words.words()
    print("guess" in english_words)
    word=get_random_word()
    guesses=["_"*5]*6
    for idx in range(6):
        refresh_page(headline=f"Guess {idx+1}")
        show_guesses(guesses,word)
        while True:
            try:
                guesses[idx]=input("\nGuess word: ").upper()
                if len(guesses[idx])!=5:
                    raise ValueError #this will send it to the print message and back to the input option
                if guesses[idx].lower() not in english_words:
                    raise ValueError #this will check the word is in the english dictionary
                break
            except ValueError:
                console.print("[red bold]Invalid input.\n The word must be 5 letters long and in the english dictionary")
        if guesses[idx]==word:
            print("correct")
            break 
    else:
        game_over(word)
refresh_page("wordle")
if __name__=="__main__":
    main()
