import random

# Converts list into English (e.g. ["a", "b", "c"] becomes "a, b, and c")
def sentenceify(inputList):
    if len(inputList) == 1:
        return inputList[0]
    else:
        return "{} and {}".format(", ".join(inputList[:-1]), inputList[-1])

candidates = None
outCandidates = []
ballots = []

if input("Will you open from a file (y/n)? ") == "y":
    file = open(input("What is the name of the file (with extension)? "), "r")
    fileLines = [line.strip() for line in file.readlines()]
    candidates = {i:0 for i in fileLines[0].split()}
    ballots = [line.split() for line in fileLines[1:]]
    file.close()
else:
    {i:0 for i in input("Please enter the candidates: ").split()}
    
    while True:
        ballot = input("Please enter a ballot or leave blank to finish: ").split()
        
        if ballot: ballots.append(ballot)
        else: break

majorityReached = False

while not majorityReached:
    # Resets all candidate votes
    candidates = dict.fromkeys(candidates, 0)
    
    # Counts the ballots
    for ballot in ballots:
        candidates[ballot[0]] += 1
        print("Ballot {} goes to {}".format(sentenceify(ballot), ballot[0]))
    
    # Line break
    print()
    
    # Announces the results
    for candidate in candidates.keys():
        # If a majority has been reached,
        if candidates[candidate] > len(ballots) / 2:
            # Announce your votes and that a majority has been reached
            majorityReached = True
            print("{} has {}/{} votes and reaches a majority".format(candidate, candidates[candidate], len(ballots)))
        else:
            # Otherwise, announce your votes
            print("{} has {}/{} votes".format(candidate, candidates[candidate], len(ballots)))
    
    if not majorityReached:
        # Finds the least voted candidates
        leastVoted = [candidate for candidate in candidates.keys() if candidates[candidate] == min(candidates.values())]
        leastVotedStr = [str(i) for i in leastVoted]
        
        # If there is a tie, announce that there is a tie
        if len(leastVoted) > 1:
            print("{} are tied, elimination will be random".format(sentenceify(leastVoted)))
        
        # Eliminates and announces a random candidate from the leastVoted list
        outCandidate = random.choice(leastVoted);
        del candidates[outCandidate]
        outCandidates.append(outCandidate)
        print("{} has been eliminated\n".format(outCandidate))
        
        # Removes eliminated candidates from the ballots while keeping a copy of the old ballots
        oldBallots = ballots
        ballots = [[choice for choice in ballot if not choice in outCandidates] for ballot in ballots]
        
        # Announces the changes in the ballots
        for ballotIndex in range(len(ballots)):
            oldBallot = oldBallots[ballotIndex]
            newBallot = ballots[ballotIndex]
            
            if oldBallot != newBallot and newBallot:
                print("Ballot {} becomes ballot {}".format(sentenceify(oldBallot), sentenceify(newBallot)))
            elif not newBallot:
                print("Ballot {} is removed".format(sentenceify(oldBallot)))
            else:
                print("Ballot {} stays the same".format(sentenceify(oldBallot)))
        
        # Removes empty ballots
        ballots = [ballot for ballot in ballots if ballot]
        
        # Announces new round
        print("\nNEXT ROUND\n")