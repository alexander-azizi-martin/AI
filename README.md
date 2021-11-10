# Knights

A program to solve the three Knights and Knaves puzzles listed below using propositional logic. 

In a Knights and Knaves puzzle, the following information is given: Each character is either a knight or a knave. 
A knight will always tell the truth: if knight states a sentence, then that sentence is true. Conversely, a knave will always lie: 
if a knave states a sentence, then that sentence is false. 

The objective of the puzzle is, given a set of sentences spoken by each of 
the characters, determine, for each character, whether that character is a knight or a knave.

## Puzzles

Puzzle 0 contains a single character: A.
  - A says “I am both a knight and a knave.”
  
Puzzle 1 has two characters: A and B.
- A says “We are both knaves.”
- B says nothing.

Puzzle 2 has two characters: A and B.
- A says “We are the same kind.”
- B says “We are of different kinds.”

Puzzle 3 has three characters: A, B, and C.
- A says either “I am a knight.” or “I am a knave.”, but you don’t know which.
- B says “A said ‘I am a knave.’”
- B then says “C is a knave.”
- C says “A is a knight.”

## Usage

```
$ python puzzle.py
Puzzle 0
    A is a Knave
Puzzle 1
    A is a Knave
    B is a Knight
Puzzle 2
    A is a Knave
    B is a Knight
Puzzle 3
    A is a Knight
    B is a Knave
    C is a Knight
```
