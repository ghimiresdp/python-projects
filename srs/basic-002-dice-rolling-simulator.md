- **created by**: Sudip Ghimire
- **URL**: https://www.sudipghimire.com.np
- **GitHub**: https://github.com/ghimiresdp

<h3>[Go to Index](https://github.com/ghimiresdp/python-projects/)</h3><hr>

# SRS: Dice Rolling Simulator

> **Prerequisite**
> - Basic understanding of functions and functional programming
> - Understanding of `modules and packages`
> - Basic understanding of a python [random](https://docs.python.org/3/library/random.html) module

**Table of Contents**

- [SRS: Dice Rolling Simulator](#srs-dice-rolling-simulator)
    - [1. Introduction](#1-introduction)
    - [2. Functional Requirements](#2-functional-requirements)
        - [2.1. Dice Rolling](#21-dice-rolling)
        - [2.2 Display the Statistics](#22-display-the-statistics)
    - [3. Non-functional Requirements](#3-non-functional-requirements)
        - [3.1. User Interface](#31-user-interface)
    - [References:](#references)

## 1. Introduction

The Dice Rolling Simulator Application is a software tool designed to simulate
the rolling of dice. The application aims to provide users with a virtual dice
rolling experience for recreational purposes, games, or other dice-related
activities.

## 2. Functional Requirements

### 2.1. Dice Rolling

The Dice Rolling Simulator Application should provide the following features
for dice rolling:

1. Specify the number of dice to roll
2. Specify the number of sides on each die
3. Show the results of all dice and the sum of those on every roll.

### 2.2 Display the Statistics

User should be able to see the statistics of the game such as:

1. total number of `6` rolled
2. the number that rolled maximum times throughout the game
3. the average of all the numbers rolled in the game

## 3. Non-functional Requirements

### 3.1. User Interface

The interface should ask user to input the number of dices to roll at the start
of the game.

```
-------------------------------------------------------
ROLL THE DICE
-------------------------------------------------------
Enter the number of die to roll [0 to exit]:
```

After entering the number of dice to roll, user should get a prompt to enter
to roll the dice. The prompt should also accept options to exit from the game.

```
-------------------------------------------------------
ROLL THE DICE
-------------------------------------------------------
Enter the number of die to roll [0 to exit]: 3
-------------------------------------------------------

Rolling the dice ...

Die 1:  1
Die 2:  4
Die 3:  2

sum:                     9
total rolls              4
maximum occurrence:      1
-------------------------------------------------------
Enter to roll [0 to exit]:

```

## References:

- **Python Notes:
  ** [chapter 8 Modules and Packages](https://github.com/ghimiresdp/python-notes/blob/main/c08_modules_packages/chapter%208.4%20random.md)
- **Official Documentation**: [Random Module](https://docs.python.org/3/library/random.html)
