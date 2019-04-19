# IRV Algorithm
An algorithm for Instant-Runoff Voting elections.

[Run online](https://repl.it/@hablabemails/IRV-Algorithm-v2)
[Run old version](https://repl.it/@hablabemails/IRV-Algorithm)

## What's Instant-Runoff Voting?
Simply put, [Instant-Runoff Voting (IRV)](https://en.wikipedia.org/wiki/Instant-runoff_voting) is a voting system for electing one winner, designed to simulate many elections where one candidate is eliminated in each round, without the impracticality of holding multiple elections. It is also known as the alternative vote and preferential voting.

The voters, instead of only choosing one person on their ballot, can rank their choices from best to worst. They can vote for as many or as few candidates as they wish.
```
[ ] Alex | [1] Alex | [2] Alex
[1] Bill | [ ] Bill | [3] Bill
[2] Carl | [ ] Carl | [1] Carl
```
Then, if there is no majority, the least popular candidate is eliminated from the election, and that candidate's votes are redistributed according to the voter's second choice votes.
```
-------- <- MAJORITY
[] []
[] []
[] [] []
A  B  C
```
C is eliminated.
C's voters chose B for their second choice.
```
---[] <- MAJORITY
[] []
[] []
[] []
A  B
```
B is elected.

## How to use
### Creating a file
1. The first line of a file should contain the names of the candidates, separated by spaces.
```
Alex Bill Carl
```
2. The rest of the lines should contain the ballots in order of ranking on the ballot, separated by spaces (unmarked candidates should just be ignored).
```
+==========+==========+===========+
| [ ] Alex | [1] Bill | Bill Carl |
| [1] Bill | [2] Carl |           |
| [2] Carl |          |           |
+==========+==========+===========+
+==========+==========+===========+
| [1] Alex | [1] Alex | Alex Carl |
| [ ] Bill | [2] Carl |           |
| [2] Carl |          |           |
+==========+==========+===========+
etc.
```
```
Bill Carl
Alex Carl
etc.
```
3. The file should be saved as a text file in the same folder as the algorithm.
```
.../Downloads/irv.py
.../Downloads/myFile.txt
```

### Importing a file
1. Enter "0" when asked which option to select.
```
[0] Import file
[1] Random test
Which option? 0
```
2. Write the name of the file _without_ the extension (the `.txt` at the end).
```
.../Downloads/irv.py
.../Downloads/myFile.txt
```
```
What is the name of the file (without the extension)? myFile
```
### Randomly generating a test
As the name suggests, this is mainly designed for testing the program by randomly generating a certain number of ballots. It does _not_ create a file.

1. Enter "1" when asked which option to select.
```
[0] Import file
[1] Random test
Which option? 1
```
2. Write the number of candidates and ballots you want.
```
How many candidates are there? 10
How many ballots are there? 1000000
```
