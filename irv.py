import re

candidates = {i:0 for i in range(int(input("How many candidates? ")))}
outCandidates = []

ballots = input("Please enter the ballots ").split()
majorityReached = False

while not majorityReached:
    # Resets all candidate votes
    candidates = dict.fromkeys(candidates, 0)
    
    # Counts the ballots
    for ballot in ballots:
        candidates[int(ballot[0])] += 1
        print("Ballot {} goes to Candidate {}".format(ballot, ballot[0]))
    
    # Line break
    print()
    
    # Announces the results
    for candidate in candidates.keys():
        # If a majority has been reached,
        if candidates[candidate] > len(ballots) / 2:
            # Announce your votes and that a majority has been reached
            majorityReached = True
            print("Candidate {} has {}/{} votes and reaches a majority".format(candidate, candidates[candidate], len(ballots)))
        else:
            # Otherwise, announce your votes
            print("Candidate {} has {}/{} votes".format(candidate, candidates[candidate], len(ballots)))
    
    if not majorityReached:
        # Finds the least voted candidates
        leastVoted = [candidate for candidate in candidates.keys() if candidates[candidate] == min(candidates.values())]
        leastVotedStr = [str(i) for i in leastVoted]
        
        # If there is a tie, announce that there is a tie
        if len(leastVoted) > 1:
            print("Candidates {} and {} are tied, elimination will be random".format(", ".join(leastVotedStr[:-1]), leastVoted[-1]))
        
        # Eliminates and announces the first candidate in the leastVoted list
        del candidates[leastVoted[0]]
        outCandidates.append(str(leastVoted[0]))
        print("Candidate {} has been eliminated\n".format(leastVoted[0]))
        
        # Removes eliminated candidates from the ballots while keeping a copy of the old ballots
        oldBallots = ballots
        ballots = [re.sub("|".join(outCandidates), "", ballot) for ballot in ballots]
        
        # Announces the changes in the ballots
        for ballotIndex in range(len(ballots)):
            oldBallot = oldBallots[ballotIndex]
            newBallot = ballots[ballotIndex]
            
            if oldBallot != newBallot and newBallot != "":
                print("Ballot {} becomes ballot {}".format(oldBallot, newBallot))
            elif newBallot == "":
                print("Ballot {} is removed".format(oldBallot))
            else:
                print("Ballot {} stays the same".format(oldBallot))
        
        # Removes empty ballots
        ballots = [ballot for ballot in ballots if ballot != ""]
        
        # Announces new round
        print("\nNEXT ROUND\n")