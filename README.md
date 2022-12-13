# WORDLE  

Wordle is a word guessing game. It gives players six chances to guess a randomly selected five-letter word. The player's guess is reflected onto the pygame screen. As shown above, if you have the right letter in the right spot, it turns green. A correct letter in the wrong spot turns yellow. A letter that isn't in the word in any spot turns gray.

## PlAYING THE GAME 

- Install the necessary libraries
    - Make sure to install 'pygame,' 'sys,' and 'english_words'
- To play the game, you will be prompted with the terminal asking for your guess. For this input, type in the terminal a five letter word to guess the randomly selected five-letter word. 
- If you put in a word that contains numbers or symbols, the terminal will tell you that you need to put in a five-letter word.
- If you want to quit the game without finishing all your tries, type in 'q' for your guess. Once you do this, the game will tell you what the word was and then quit the game.
- Once you run out of tries without getting the word correct, the pygame screen will tell you you are out of tries and then tell you what the correct word was.
- If you get the word correct within your six tries, the pygame will display a congratulatory message and say how many tries it took you to get the word right.

Rules:

- Each guess must be a valid five-letter word.
- Each guess must only contain letters and not numbers or symbols.


## FEATURES 

- Six rows of five-letter words
- Color-coded boxes to indicate correct and incorrect guesses

## KNOWN LIMITATION 

- Only includes five-letter words from the English language

Note: This game runs best on a Mac computer; we have seen issues with the pygame screen not updating correctly when it is played on Windows.