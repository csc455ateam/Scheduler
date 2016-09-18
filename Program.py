#!/usr/bin/python

'''
Program: Linda's Bar and Grill Scheduling application
Author: Christian M. Adams

This is a prototype of a mobile application for Linda's Bar and Grill in Chapel Hill, NC that will allow employees to manage and reschedule their shifts on the fly in a way that updates in real time.  


Functionality to be implemented:
  1. This would send a push notification to the phones of all people involved with the schedule change.  
  2. When a shift change is requested, it would need to be approved by the manager first.
  3. Override permissions for Owner (Chris Carini)
  4. GUI
  5. Ability to submit a master schedule every 2 weeks by manager
  6. Keep a record of past schedules
  7. Tally up hours worked based on the schedule
  8. Create a report for each employee
  9. Ability to input sales for the night and calculate tip-out

Administrater/Owner Tools:
	1. Ability to input sales per night by Manager

Information:
	1. Usual staffing during the day: 1 chef, 2 bartenders, 1 barback
	2. Usual staffing after 5pm: 1 chef, 3 bartenders, 2 barbacks
	
GUI will have a calendar much like google.calendar's apps. 

Ultimately will be run with a LAMP stack using Python as the 'P' of the stack.  

'''

#IMPORTS
from menu import *
import random
from employee import *
from Scheduler import *
import clserver
import clclient

#Global Variables
empList = []


#MENU
def menuChoice():
    try:
        mainChoice = int(initMenu())
    except: print("Invalid Input")
    if (mainChoice == 1):
        empUser = input("Enter your user name: ")
        empPass = input("Enter your password: ")
        while True:
            empChoice = int(empMenu())
            if empChoice == 'error':
                print(mainChoice)
            #View Schedule
            elif empChoice == 1:
                viewSchedule()
            #Switch Shift - changes the 
            elif empChoice == 2:
                print("[here in Swap Shift]")
            #Request Off
            elif empChoice == 3:
                pass
            #Hours Count - References a text file of past hours, and adds current hours from current week (labeled and separate)
            elif empChoice == 4:
                pass
            #Chatroom - will have to save messages to a text file and report them in real time on a GUI
            elif empChoice == 5:
                clclient()
            elif empChoice == 6:
                break
    elif mainChoice == 2:
        empUser = input("Enter your user name: ")
        empPass = input("Enter your password: ")
        while True:

            #Admin Tools
    #        elif mainChoice == 5:
            adminChoice = int(adminMenu())
            #View Schedule
            if adminChoice == 1:
                addEmployee()
            #Submit Event Schedule
            elif adminChoice == 2:
                pass
            #Propose Schedule Change
            elif adminChoice == 3:
                pass
            #Lists Current Employees
            elif adminChoice == 4:
                listEmployee()
            elif adminChoice == 5:
                 #makes new schedule for the week
                sch = schedule(getshifts(), getavail())
                sch = str(sch)                                          ###Sch needs to be changed/formatted for the viewSchedule

                #write to a file to be read by viewSchedule() function
                f = open("currentSchedule.txt", 'w')
                f.write(sch)     
                f.close()                                                           ###
                viewSchedule()
            #View current Schedule
            elif adminChoice == 6:
                viewSchedule()
            #Exit/logout
            elif adminChoice == 7:
                break
#    #Cancel - return to main menu
#    elif adminChoice == 3:
#      #exit
#        break
    else:
        print("\n---Please enter a number between 1 and 3")




def viewSchedule():
  print("[Display Schedule Here]")
  #must be able to read a text file schedule and display it in a readable fashion
  file = open("currentSchedule.txt",'r')
  lines = file.read().splitlines()
  print(lines)
  
def addEmployee():
  fname = str(input("What is the first name of the new employee?"))
  lname = str(input("What is their last name?"))
  dayPref = str(input("What days would you like to work? \n (1) Mon \n (2) Tues \n (3) Wed \n (4) Thu \n (5) Fri \n (6) Sat \n (7) Sun \n"))
  hoursPref = str(input("(1) Early shift \n(2) Night shift\n"))
  id = genEmpNum(fname, lname)
  worker = employee(fname, lname, dayPref, hoursPref, id)
  print("Employee "+fname, lname, "has ID number: ", id)
  empList.append(worker)
  
  
  
def delEmployee():
    print("[Need to add delete function here]")
    
def listEmployee():
    print("Current Employees: \n")
    for item in empList:
      print(item.getFullName())
  
def genEmpNum(fname, lname):
    id = fname[0] + lname[0]
    id = id.upper()
    rnum = random.randint(1000, 9999)
    rnum = str(rnum)
    id = id + rnum
    print("{0}'s new ID code is {1}." .format(fname, id))
    return id


def main():
#  clserver()
  while True:
    menuChoice()
    
  
  
if __name__ == "__main__":
  main()