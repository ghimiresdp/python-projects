# Project: Rock Paper Scissor

## prerequisites:
- Basic Object-Oriented Programming knowledge
- `random` library

Rock Paper Scissors is a multi-player game that is played by showing different symbols randomly.
For Example you and your friend show the the random symbol  The symbols are as follows:

- **Rock** 👊
- **Paper** 🤚
- **Scissors** ✌️


Game Rules:

- `Rock` breaks the `Scissor`
- `Scissor` cuts the `Paper`
- `Paper` covers the `Rock`

## Instructions

1. use random library for generating random numbers
2. assign values:
   ```
    1. ROCK
    2. SCISSOR
    3. PAPER
   ```
3. create an infinite loop that is capable to show user to input numbers that represents rock, paper, and scissor.
4. If the user guesses the same as the machine, it becomes draw.
5. If any side beats for consecutive 3 times, then they win the game. i.e. if you beat computer for 2 times and the computer beats you again, then the count will be reset and the match will continue

## Example user interface:

```
Welcome to Rock Paper Scissor Game

please enter your name to continue:     John

1. ROCK
2. SCISSOR
3. PAPER

0. Quit Game
9. Restart Game

ROCK-PAPER-SCISSOR: 1

John     : ROCK
Computer : SCISSOR

+-------------------------------------------------------+
|                      Game Statistics                  |
+.......................................................+
|  Total Rounds:     1      |  Total Draws:      0      |
|  Computer:         0      |  John:             1      |
|                                                       |
|   +-----------------------------------------------+   |
|   |                   YOU WON!                    |   |
|   +-----------------------------------------------+   |
|                                                       |
+-------------------------------------------------------+

1. ROCK
2. SCISSOR
3. PAPER

0. Quit Game
9. Restart Game

ROCK-PAPER-SCISSOR: 3

John     : PAPER
Computer : SCISSOR
+-------------------------------------------------------+
|                      Game Statistics                  |
+.......................................................+
|  Total Rounds:     2      |  Total Draws:      0      |
|  Computer:         1      |  John:             1      |
|                                                       |
|   +-----------------------------------------------+   |
|   |                 COMPUTER WON!                 |   |
|   +-----------------------------------------------+   |
|                                                       |
+-------------------------------------------------------+

1. ROCK
2. SCISSOR
3. PAPER

0. Quit Game
9. Restart Game

ROCK-PAPER-SCISSOR:
```

If you win for 3 consecutive times, it should show `CONGRATULATIONS, YOU WON THE MATCH`


```
John     : Rock
Computer : SCISSOR
+-------------------------------------------------------+
|                      Game Statistics                  |
+.......................................................+
|  Total Rounds:     2      |  Total Draws:      0      |
|  Computer:         1      |  John:             3      |
|                                                       |
|   +-----------------------------------------------+   |
|   |      CONGRATULATIONS, YOU WON THE MATCH       |   |
|   +-----------------------------------------------+   |
|                                                       |
+-------------------------------------------------------+

0. Quit Game
9. Restart Game

ROCK-PAPER-SCISSOR:
```
