#CTI 110
#p4hw1 Score Average
#Jeremiah Grafals
#3-18-2022

###gets all scores
##score1 = float(input('Enter score #1: '))
##score2 = float(input('Enter score #2: '))
##score3 = float(input('Enter score #3: '))
##score4 = float(input('Enter score #4: '))
##score5 = float(input('Enter score #5: '))
##score6 = float(input('Enter score #6: '))
##score7 = float(input('Enter score #7: '))
##
###makes a list
##scores = [score1,score2,score3,score4,score5,score6,score7]

#Initializes/Declares variables & makes scores list
scores = []
i = 0
score = int()

#Gets number of scores to be entered
numscores = int(input('Enter number of scores: '))

#Gets scores
while i < numscores:
    score = int(input(f'Enter score #{i + 1}: '))
    #Determines if score is less than zero or greater than 100
    if 0 > score or score > 100:
        print('Invalid Entry!\nEntry must be between 0 and 100!')
        i = i
    else:
        scores.append(score)    #Adds each score to end of list
        i += 1

#finds lowest score and removes it
print("----Results-----")
min_score = min(scores)
print('Lowest score:',min_score)
scores.remove(min_score)
print('Modified list:',scores)

#averages scores list
average = sum(scores)/len(scores)
print('Average score:',format(average,'.2f'))

#Determines letter grade
if 100 >= average >= 90:
    print('Letter Grade: A')
elif 89 >= average >= 80:
    print('Letter Grade: B')
elif 79 >= average >= 70:
    print('Letter Grade: C')
elif 69 >= average >= 60:
    print('Letter Grade: D')
elif 59 >= average >= 0:
    print('Letter Grade: F')
