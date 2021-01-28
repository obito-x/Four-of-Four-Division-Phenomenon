# Fourty Division Phenomenon
#
# Question:
# How can you divide 40 to 4 parts such that every 
# number from 1-40 can be realized just by adding or subtracting
# those 4 parts?
#
# This program is base on Pobability and Programming Task.
# Not a Formal Math Caculation.

import json
from algorithm import algorithm

with open('fourty_division_data.json', 'r') as jsonData:
    data = json.load(jsonData)

answer = 0
all_caculation_answers_list = []

for d in data:
	# All Possible Caculation
	test = algorithm(d) 

	# Testing with 40
	if(len(test) > 40):
		if(test[:40] == [i for i in range(1,41)]):
			answer = d
			all_caculation_answers_list = test[:40]

# Ouput the Result
if answer != 0:
	algorithm(answer, verbose=True)
	print("\nThe Four of Fourty Division Phenomenon: ", answer)
	print("Ansers: \n")
	for num in all_caculation_answers_list: # Printing in Formatly
		print(f"{num:2.0f}", end="")
		if((all_caculation_answers_list.index(num) + 1)%10 == 0):
			print("\n")
		else:
			print(" ", end="")
else:
	print("Program Fail! or Not Found!!")
