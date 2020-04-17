#Dependencies
import os
import csv

#Looking for the csv file
csvpath= os.path.join('Resources', 'election_data.csv')

# Open and reading the CSV file
with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    
    #total votes
    count = 0
    candidateList = []
    candidateVotes = []

    # Iterate through rows
    for row in csvreader:
        # Define count of votes
        count += 1

        #Define candidates row
        candidate = row[2]

        if candidate in candidateList:
            candidateIndex = candidateList.index(candidate)
            candidateVotes[candidateIndex] = candidateVotes[candidateIndex] + 1
        else:
            candidateList.append(candidate)
            candidateVotes.append(1)
        
    print(f"Total votes {count}")
    # print(f"Each candidate: {candidateList}")
    # print(f"Index: {candidateList.index(candidate)}")
  
    #to capture the percentage of votes of each candidate
    percentage = []
    maxVotes = candidateVotes[0]
    max_index = 0

    for x in range(len(candidateList)):
        votePercent = round(candidateVotes[x]/count*100,2)
        percentage.append(votePercent)

        if candidateVotes[x] > maxVotes:
            max_index = x
    winner = candidateList[max_index]

    # print(f"Vote count for each candidate: {candidateVotes}")
    # print(f"Max votes: {maxVotes}")
    # print(f"Election winner: {winner}")

    print("Election Results")
    print("-----------------------")
    print(f"Total Votes : {count}")
    print("-----------------------")
    for x in range(len(candidateList)):
        print(f"{candidateList[x]}: {percentage[x]}% ({candidateVotes[x]})")
    print("-----------------------")
    print(f"Winner : {winner}")

# Export to txt file
    txtfile = open("txtfile.txt", "w")

    line1 = "Election Results"
    line2 = "---------------------"
    line3 = str(f"Total Votes : {count}")
    line4 = "---------------------"
    for x in range(len(candidateList)):
        line5 = str(f"{candidateList[x]}: {percentage[x]}% ({candidateVotes[x]})")
    line6 = "---------------------"
    line7 = str(f"Winner : {winner}")
    txtfile.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))
