__author__ = "Anthony Chase Parker"

import os

"Generic scheduling application for allocating employee shifts based on available hours"
"and shifts needed."


def main():
    days = ["Su", "M", "T", "W", "Th", "F", "S"]
    global shift_loc
    global avail_loc

    # call getshifts() and getavail() function with file path info as param
    ls_shifts = getshifts()
    ls_avail = getavail()
#    print(ls_shifts)
#    print(ls_avail)
#    final_sched = schedule(ls_shifts, ls_avail)
#    print(final_sched)


"""
Function used to obtain list of needed daily shifts
Directory selection available
@param f_loc Location of needed shifts file
@return ls_temp List of shifts needed for each day
"""

def getshifts():
    ls_temp = []
    shift_loc = input("Please enter the location of your shifts needed information or type 'C' to use "
          "current directory: ")
    if shift_loc is "C" or shift_loc is "c":
      shift_loc = os.path.dirname(os.path.abspath(__file__)) + "/shifts.txt"
    with open(shift_loc) as f:
        ls_lines = f.read().splitlines()
        # iterate over each line in list of line strings
        for i in ls_lines:
            # split each line into list of words
            t_lines = i.split()
            t_temp = []
            # iterate through list of words
            for j in t_lines:
                # ignore day of week (first index)
                if j == t_lines[0]:
                    continue
                t_temp.append(j)
            ls_temp.append(t_temp)
    # return list composed of tuples whose index references their corresponding day
    return ls_temp


def getmaxhours():
    pass


"""
Function used to obtain a dictionary of Name:Availability pairs. Availability contains
a list of time slots the employee can be scheduled corresponding to each day of the
week from Sunday to Saturday.
Directory selection available.
@param f_loc Location of availability information file
@return d_temp Dictionary containing Name:Availability pairings
"""

def getavail():
    d_temp = {}
    ls_temp = []
    avail_loc = input("Please enter the location of your availability information or type 'C' to use "
          "current directory: ")
    if avail_loc is "c" or avail_loc is "C":
      avail_loc = os.path.dirname(os.path.abspath(__file__)) + "/avail.txt"
    # label counter (explained below)
    ct = 0
    with open(avail_loc) as f:
        ls_lines = f.read().splitlines()
        # iterate over every line in the availability text file
        for i in ls_lines:
            # counter keeps day labels from being included in availability data
            if ct == 0:
                ct += 1
                continue
            # split line into list of strings
            t_lines = i.split()
            # iterate over words in list
            for j in t_lines:
                # use first column word as key (Name of employee)
                if j == t_lines[0]:
                    key = j
                    continue
                ls_temp.append(j)
            # add dictionary item as Name:[AvailabilityList] pair with value indexes as days
            d_temp[key] = ls_temp
            ls_temp = []
    # return dictionary of Name:[AvailabilityList] pairs
    return d_temp


"""
Function used to create work schedule based on employee availability and necessary shifts.
@param shifts,avail Lists of shifts needed and employee availability dictionaries
@return ls_final List containing final calculated schedule
"""

def schedule(shifts, avail):
    ls_final = []
    # day counter, can be modified to allow for multi-week scheduling
    day = 0
    # iterate over each shift needed tuple in the list
    for i in shifts:
        ls_temp = []
        # iterate over each time-slot needed in each tuple of list
        for j in i:
            # counter prevents double scheduling of employee
            ct = 0
            # split each time-slot into workable text to be used as integers later
            t_shift = j.split(':')
            # iterate over each key:value pair in availability dictionary
            for key, value in avail.items():
                # if employee has specific availability, favor that request
                if value[day] != 'Any' or value[day] != 'Off':
                    # split employee availability into workable numbers
                    av_temp = value[day].split(':')
                    # if employee avail. falls in range, schedule employee
                    if av_temp != 'Off' or av_temp != 'Any':
                        if av_temp[0] <= t_shift[0]:
                            if av_temp[1] >= t_shift[1]:
                                ls_temp.append((key, j))
                                value[day] = "Used"
                                # change counter to prevent employee double-scheduling
                                ct = 1
                                break
                # if employee day says 'Any,' schedule employee for time-slot
                if value[day] == 'Any':
                    ls_temp.append((key, j))
                    value[day] = "Used"
                    # change counter to prevent employee double-scheduling
                    ct = 1
                    break
                if ct == 1:
                    break
        # call shortstaffed function if some shift is not fulfilled
        if len(ls_temp) != len(shifts[day]):
            ls_temp = shortstaffed(ls_temp)
        ls_final.append(ls_temp)
        # move to next day
        day += 1
    # return final schedule list of lists corresponding to Day/Shift
    return ls_final


"""
Function used to notify management of possible missing shifts given labor
requirements and employee availability information
@param list List of final schedule
@return list Modified list with warnings about possible missing shifts
"""

def shortstaffed(list):
    list.append("Missing Shift")
    return list

if __name__ == "__main__":
  main()


