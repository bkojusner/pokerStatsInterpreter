# pokerStatsInterpreter
Little project on the Chen Formula and how one would apply it in-game

Currently just a script which analyzes what hand is given and determines what would be appropriate action to take pre-game with the hand that is given and the amount of people that are playing. None of the inputs are case sensitive.

# Usage
 - **Hand:** You type in the letter representation of your card, followed by a space and the representation of the second card. If the cards are suited then enter the letter s at the end of the input.
    - e.g. If you had Ace Ten Suited you would type ```a 10 s``` (note: a, k, q, j are only letters, everything else should be the number)
 - **Rating:** This is the value given to your hand after it has been calculated using the Chen Formula
 - **[F]ull ring (10) or [S]hort handed (6):** Here you type either ```F``` for full ring, 10 people or less playing, or you type ```S``` for short handed, which implies 6 people or less
 - **[E]arly, [M]id, or [L]ate position:** Here you type either ```E```, ```M```, or ```L``` to indicate what position your playing with respect to the hand
 - **Verdict:** The program will then give you a verdict as to what it thinks you should do, pre-game, given the scenario at hand
 - The program runs in a loop to take input without exiting. If one wanted to exit, they would simply type ```exit``` on the ```Hand:``` prompt and the program will respond with a successful exit message
