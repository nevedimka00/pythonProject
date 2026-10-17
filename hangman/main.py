import random
from words_list import words


hangman_art = {0:("   ",
                  "   ",
                  "   "),
               1:(" o ",
                  "   ",
                  "   "),
               2:(" o ",
                  " | ",
                  "   "),
               3:(" o ",
                  "-| ",
                  "  "),
               4:(" o ",
                  "-|-",
                  "   "),
               5:(" o ",
                  "-|-",
                  "/ "),
               6:(" o ",
                  "-|-",
                  "/\\"),}

def display_man(wrong_guesses):
    print("*"*10)
    for l in hangman_art[wrong_guesses]:
        print(l)
    print("*"*10)

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def check_game_status(wrong_guesses,answer,guessed_letters,hint):
    if wrong_guesses==6 :
        display_man(wrong_guesses)
        display_answer(answer)
        print(f"Wrong letters : {guessed_letters}")
        print("You lost!")
        return False
    elif not hint.__contains__("_"):
        display_answer(answer)
        print(f"Wrong letters : {guessed_letters}")
        print("You won!")
        return False
    else: return True

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running=True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()

        if len(guess)>1 or guess.isdigit():
            print("Invalid input")
            continue

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i]=guess
        else:
            guessed_letters.add(guess)
            wrong_guesses+=1
        is_running=check_game_status(wrong_guesses,answer,guessed_letters,hint)


if __name__=="__main__":
    main()