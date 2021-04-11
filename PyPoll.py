import os
import csv

csvpath = os.path.join('election_data.csv')

total_votes = 0
total_candidates = 0
percent_votes = []
candidate_options = []
candidate_votes = {}
greatest_votes = ["", 0]


with open (csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csv_reader)

    

    # total number of votes
    for row in csv_reader:
        total_votes = total_votes + 1
        total_candidates = row["Candidate"]


    # complete list of candidates who received votes
        candidate_votes[row["Candidate"]] = 1

    # Percentage of votes each candidate won
    
        percentage = (votes/total) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        percent_votes.append(percentage)


    # Total number of votes each candidate won
        
        candidate_votes = total_votes.count
        
        
    # The winner of the election basde on popular vote 
        winner = max(total_votes)
        index = total_votes.index(winner)
        winning_candidate = total_candidates[index]


total_votes = sum(total_votes)
print(total_sum)
print(winning_candidate)
print(percent_votes)

