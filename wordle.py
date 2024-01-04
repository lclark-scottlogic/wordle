from nltk.corpus import words
from rich.console import Console
from helper_functions import get_random_word,refresh_page,show_guesses,game_over
console = Console(width=40)
def main():
    english_words = words.words()
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
            game_over(guesses, word, guessed_correctly=guesses[idx]==word)
            break 
    else:
        game_over(guesses, word, guessed_correctly=guesses[idx]==word)
if __name__=="__main__":
    main()
