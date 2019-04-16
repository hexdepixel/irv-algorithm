# IRV Algorithm
An algorithm for Instant-Runoff Voting elections.

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
## ##
## ##
## ## ##
A  B  C

C is eliminated.
C's voters chose B for their second choice.

---##--- <- MAJORITY
## ##
## ##
## ## ##
A  B  C

B is elected.
```
## How to use
### Manual input
1. First, enter the names of the candidates, separated by spaces.
```
Please enter the candidates: Alex Bill Carl
```
2. Then, enter the ballots in order of ranking on the ballot, separated by spaces (unmarked candidates should just be ignored). Keep doing this until you have entered all of the ballots.
```
[ ] Alex | [1] Bill | Bill Carl
[1] Bill | [2] Carl |
[2] Carl |          |
```
```
Please enter a ballot or leave blank to finish: Bill Carl
```
3. When you are finished, leave the ballot input blank and press `ENTER`. The election should start.
```
Please enter a ballot or leave blank to finish: 
...
```
### Importing a file
1. The first line of a file should contain the names of the candidates, separated by spaces.
```
Alex Bill Carl
```
2. The rest of the lines should contain the ballots in order of ranking on the ballot, separated by spaces (unmarked candidates should just be ignored).
```
[ ] Alex | [1] Bill | Bill Carl
[1] Bill | [2] Carl |
[2] Carl |          |
```
```
Bill Carl
```
3. To open the file, answer `y` to the question "Will you open from a file?" and enter the full name of your file, including its extensions. The file should be in the same folder as the algorithm.
```
Will you open from a file (y/n)? y
What is the name of the file (with extension)? test.txt
```
