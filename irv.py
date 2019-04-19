import random
import time

file = {}

print("[0] Import file")
print("[1] Random test")

# Imports a file and returns a dictionary with its contents, split into candidates and ballots.
# (NOT the function called by pressing 0.)
def fileToData(fileName):
	# Creates the dictionary.
	data = {}

	# Opens the file.
	with open(fileName + ".txt", "r") as file:
		# Makes a list of the file's lines (without whitespace characters like \n).
		fileLines = [line.strip() for line in file.readlines()]

		# Makes a list of candidates from the first line
		data["candidates"] = fileLines[0].split()

		# Makes a list of ballots from the rest of the lines
		data["ballots"] = [line.split() for line in fileLines[1:]]
	
	return data

# Gets the file name then executes fileToData with it. (The function called by pressing 0.)
def importFile():
	global file
	file = fileToData(input("What is the name of the file (without the extension)? "))

# Creates a random set of conditions.
def randomTest():
	# Gets the number of candidates and ballots.
	noOfCandidates = int(input("How many candidates are there? "))
	noOfBallots = int(input("How many ballots are there? "))

	# Sets the candidate names as a list of consecutive numbers.
	file["candidates"] = range(noOfCandidates)

	# Sets the ballots as lists of random candidates of random length (capped at the number of
	# candidates.)
	file["ballots"] = [[random.choice(file["candidates"]) for choice in range(random.randint(1,
	noOfCandidates))] for _ in range(noOfBallots)]

menuFunctions = [importFile, randomTest]

# Executes one of the menu functions depending on which number is pressed.
menuFunctions[int(input("Which option? "))]()

# Makes a dictionary where each candidate corresponds to a list of ballots that voted for them.
# This is so that if a candidate gets eliminated, only ballots that voted for them have to be
# cleaned and redistributed, whereas the first version cleaned and redistributed the whole list.
votes = {i:[] for i in file["candidates"]}

# Returns a dictionary where each candidate corresponds to how many ballots voted for them.
def voteCounts():
	return {candidate:len(candidateVotes) for candidate, candidateVotes in votes.items()}

# Returns the total number of valid votes.
def totalVoteCount(): return sum(voteCounts().values())

# Makes a list of ballots, which are in turn lists of choices. This will only be used once to
#distribute the ballots into the votes dictionary.
ballots = file["ballots"]

outCandidates = []
winner = None

start = time.time()

# Distributes the ballots based on first choice.
for ballot in ballots: votes[ballot[0]].append(ballot)

# The election loop. There's a break midway through the loop, so a condition isn't necessary.
while True:
	# Prints the votes while checking for a majority.
	for candidate, candidateVotes in voteCounts().items():
		# Checks for a majority (approval greater than 50% of the total votes).
		if candidateVotes > totalVoteCount() / 2: winner = candidate

		# Prints the candidate's name, how many votes they got, and the total number of votes.
		print("{} gets {}/{} votes".format(candidate, candidateVotes, totalVoteCount()))

	# Prints the winner's name and breaks the loop if there is a majority.
	if winner:
		print("{} wins".format(winner))
		break
	
	# Gets the least voted candidate(s).
	leastVoted = [candidate for candidate, candidateVotes in voteCounts().items()
	if candidateVotes == min(voteCounts().values())]

	# Randomly selects a candidate to eliminate if there is a tie for last place.
	if len(leastVoted) > 1: leastVoted = random.choice(leastVoted)
	# Eliminates the only candidate if not.
	else: leastVoted = leastVoted[0]

	# Eliminates the candidate and prints the eliminated candidate's name.
	outCandidates.append(leastVoted)
	print("{} has been eliminated".format(leastVoted))

	# Cleans the eliminated candidate's ballots by checking choice by choice if any are invalid.
	votes[leastVoted] = [[choice for choice in ballot if not choice in outCandidates]
	for ballot in votes[leastVoted]]

	# Cleans the eliminated candidate's ballots by removing empty ballots.
	votes[leastVoted] = [ballot for ballot in votes[leastVoted] if ballot]

	# Redistributes the eliminated candidate's ballots.
	for ballot in votes[leastVoted]: votes[ballot[0]].append(ballot)

	# Deletes the eliminated candidate.
	del votes[leastVoted]

end = time.time()

# Prints the amount of seconds it took for the election to complete
print("This election took {} seconds".format(end - start))
