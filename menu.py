#!/usr/bin/python

'''
Program: Menu
Author: Christian M. Adams

The follow are the menu options for Linda's BnG members.  Later, this menu will be split up into two menus, one for bands and one for venues.  
'''



def initMenu():
	print("\n\nEnter the number corresponding to the option you wish to choose")
	print("  (1) Employee Log-in \n  (2) Admin Log-in \n")
	empChoice = input("")
	return empChoice


def empMenu():
	print("\n\nEnter the number corresponding to the option you wish to choose")
	print(" (1) View Schedule \n (2) Switch Shift \n (3) Request Off \n (4) Hours Count \n (5) Chat Room \n (6) Exit")
	mainChoice = input("")
	return mainChoice

	

	
#subMenu for Band Forms


#subMenu for Scheduling
def adminMenu():
	print("\nWhat would you like to do?")
	print(" (1) Add new Employee \n (2) Submit Work Schedule \n (3) Propose Schedule Change \n (4) Employee List\n (5) Create new Schedule\n (6) Cancel")
	scheduleChoice = str(input(""))
	return scheduleChoice
	
