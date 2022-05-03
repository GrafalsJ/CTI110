#CTI 110
#p5hw2 Math Quiz
#Jeremiah Grafals
#3-29-2022

import random

def menu():
    print('Main Menu')
    print('---------------')
    print('1. Adding Random Numbers')
    print('2. Subtracting Random Numbers')
    print('3. Exit')
    print('---------------')
    print('Please choose one of the menu options above: ')
####
    
def adding():
    isanswer = False
    attempts = 1
    while isanswer == False:
        num1 = random.randint(0,999)
        num2 = random.randint(0,999)
        answer = int(input(f'{num1} + {num2} = ?\n'))
        if answer == num1+num2:
            isanswer = True
            if attempts == 1:
                print(f'Correct! It took you {attempts} attempt!')
            elif attempts != 1:
                print(f'Correct! It took you {attempts} attempts!')
        elif answer != num1+num2:
            isanswer = False
            print('Incorrect!')
            if answer > num1+num2:
                print('Your answer is too high!')
            elif answer < num1+num2:
                print('Your answer is too low!')
            attempts += 1
####        

def subtracting():
    isanswer = False
    attempts = 1
    while isanswer == False:
        num1 = random.randint(0,999)
        num2 = random.randint(0,999)
        answer = int(input(f'{num1} - {num2} = ?\n'))
        if answer == num1-num2:
            isanswer = True
            if attempts == 1:
                print(f'It took you {attempts} attempt!')
            elif attempts != 1:
                print(f'It took you {attempts} attempts!')
        elif answer != num1-num2:
            isanswer = False
            print('Incorrect!')
            if answer > num1-num2:
                print('Your answer is too high!')
            elif answer < num1-num2:
                print('Your answer is too low!')
            attempts += 1   
####
            
def main():    
    repeat = int()
    while repeat != 3:    
        menu()
        repeat = int(input())
        if repeat == 1:
            adding()
        elif repeat == 2:
            subtracting()
        else:
            print('Thank you for playing!\nGoodbye!')
main()
