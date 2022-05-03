#CTI 110
#p5hw1 Score List
#Jeremiah Grafals
#3-29-2022

def makelist(numscores):
    scores = []
    i = 0
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
    return scores
######
def calcscores(scorelist):
    lettergrade = str()

    #finds lowest score and removes it
    min_score = min(scorelist)
    scorelist.remove(min_score)

    #averages scores list
    average = sum(scorelist)/len(scorelist)

    #Determines letter grade
    if 100 >= average >= 90:
        lettergrade = 'A'
    elif 89 >= average >= 80:
        lettergrade = 'B'
    elif 79 >= average >= 70:
        lettergrade = 'C'
    elif 69 >= average >= 60:
        lettergrade = 'D'
    elif 59 >= average >= 0:
        lettergrade = 'F'

    #puts values into list
    temp = [min_score,scorelist,average,lettergrade]

    #returns list of values
    printscores(temp)

######

def listofscores():
    index = int(input('Enter number of scores: '))
    scorelist = makelist(index)
    return scorelist

######
    
def printscores(resultlist):
    
    templist = resultlist

    #takes values from returned list
    minscore = templist[0]
    newlist = templist[1]
    avg = templist[2]
    lettergrade = templist[3]

    #prints values
    print('Lowest score:',minscore)
    print('List of scores (lowest omitted):',newlist)
    print('Average:',avg)
    print('Letter Grade:',lettergrade)
#######    

repeat = 1
choice = 0
scorelist = []
while repeat != 0:
    print('----MENU----')
    print('1. Create Score List')
    print('2. Display Results')
    print('3. Exit')
    print('------------')


    choice = input()
    if choice == '1':
       scorelist = listofscores()
    elif choice == '2':
        if len(scorelist) == 0:
            print('List not created!')
        else:
            calcscores(scorelist)
    elif choice == '3':
        repeat = 0
        
print('Program Terminated!')
