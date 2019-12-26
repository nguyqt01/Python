import csv
from pprint import pprint

######################################### FUNCTIONS ####################################################################

#A funtion that reads the CSV file and make a list of lists out of the data
#Parameter: Name of CSV file user wishes to make into a List of list
#Returns: A List representation of the CSV File, an empty list if CSV is blank
def csv_to_List(fileName):
    try:
        f = open(fileName, 'r')
        reader = csv.reader(f)
        newList = []
        for row in reader:
            newList.append(row)
        f.close()
        return newList
    except:
        print('File not found.')
        exit() #Exits program if file is not found


#A listOfList map out is list[rows][columns]
#This function makes a list out of one column in a list of list starting from index 1 not default 0
#Parameters: list of lists made form a CSV file & the column number of that CSV file user wants to copy
#Return a list containing the value in a single column
def column_to_List(listOfList, columnIndex):

    clist =[]
    #Range is 1 - len because the first row in the CSV file are labels and not data
    for i in range(1,len(listOfList)):
        clist.append(listOfList[i][columnIndex])

    return clist


#A function that takes a list of strings and returns the average lenght of the strings
#Pre-condition: strList cannot be empty & contain only strings
#Parameter: a list of strings
#Return: Average lenght of string as an integer
def str_list_avg(strList):
    lenList = []
    for item in strList:
        lenList.append(len(item))         #Pre-condition avoids error popping up due to trying to divide by 0
    return int(sum(lenList)/len(lenList)) #int rounds down like project 1 directions


#A function that takes a list of int in str form and returns the average
#Pre-condition: intList cannot be empty & contain only integers
#               (Pre-condition avoids error popping up due to trying to divide by 0 & typecast failing)
#Parameter: a list of int
#Return: The average of as an integer (round Down)
def int_list_avg(intList):
    avgList = []
    for num in intList:
        avgList.append(int(num))
    return int(sum(avgList)/len(avgList)+ .5) #int rounds down in Python adding .5 make sures that rounding is accurate


#A function that find the best pilot and return a string represenation of the pilot data from list of lists produce by
#pilots training CSV data
#Pre-condition: only work specifically for the project assume every pilot took all three test
#Return list with index of Max and the max average score
def best_pilot(list_of_lists):
    ft1_scores = column_to_List(list_of_lists, 6) #list of field test 1 scores
    ft2_scores = column_to_List(list_of_lists, 7) #list of field test 2 scores
    ft3_scores = column_to_List(list_of_lists, 8) #list of field test 2 scores
    avg_Scores = []                         #empty list use to store indivduals averages

    # Add average of all three test of a pilot to the list, +.5 for int rounding down by default
    for i in range(len(ft1_scores)):
        avg_Scores.append(int( (int(ft1_scores[i]) + int(ft2_scores[i]) + int(ft3_scores[i]))/3 + .5))

    maxIndex = avg_Scores.index(max(avg_Scores)) + 1  #Adding back label row
    maxScore = max(avg_Scores)
    maxList = [maxIndex, maxScore]
    return maxList

#A function the make a dictionary to create a histogram for the color data in the pilot data
#Parameter: listoflists of CSV Pilot Data
#Return dictionary of colors and there count
def color_histogram_dict(listOfLists):

    color_dict = dict()
    color_list = column_to_List(listOfLists, 5) #Making color data into list

    #List to Dictionary with count
    for item in color_list:
        if item not in color_dict:
            color_dict[item] = 1
        else:
            color_dict[item] = color_dict[item] + 1

    return color_dict


##################################################### MAIN APP ########################################################

#Prompting User for a file name. Read in that file name. Then use the csv_to_List function to make CSV file
#into list of Lists.
filename = input('Enter a pilot data file name: ')
csvList = csv_to_List(filename)

print(csvList)
print('')

#Printing the average performance of each field test & average first/last names lenghts using functions above
print('Test Site Report:')
print('Average first name length:', str_list_avg(column_to_List(csvList,1)))
print('Average last name length: ', str_list_avg(column_to_List(csvList,2)))
print('Average field test 1 score: ', int_list_avg(column_to_List(csvList,6)))
print('Average field test 2 score: ', int_list_avg(column_to_List(csvList,7)))
print('Average field test 3 score: ', int_list_avg(column_to_List(csvList,8)))

print('')

#Printing Best Pilot Data using best_Pilot function
print('Best pilot data:')
maxList = best_pilot(csvList)
print(csvList[maxList[0]][1], csvList[maxList[0]][2], ',serial', csvList[maxList[0]][4], ',',
      csvList[maxList[0]][5], ', with an average field test score of', maxList[1])

print('')

#Color Histogram (using pretty print)
print('Colors Histogram---')
pprint(color_histogram_dict(csvList))


############################################# WRITING TO TXT ###########################################################

#Opening the txt file to be written in
FN_dot_index = filename.find('.')
filename2 = filename[:FN_dot_index] + '.txt'

#Storing in string varables the average performance of each field test & average first/last names lenghts using functions above
line1 = 'Test Site Report:' + '\n'
line2 = 'Average first name length: ' + str(str_list_avg(column_to_List(csvList,1))) + '\n'
line3 = 'Average last name length: ' + str(str_list_avg(column_to_List(csvList,2))) + '\n'
line4 = 'Average field test 1 score: ' + str(int_list_avg(column_to_List(csvList,6))) + '\n'
line5 = 'Average field test 2 score: ' + str(int_list_avg(column_to_List(csvList,7))) + '\n'
line6 = 'Average field test 3 score: ' + str(int_list_avg(column_to_List(csvList,8))) + '\n'

line7 = '\n'

#Printing Best Pilot Data using best_Pilot function
line8 = 'Best pilot data:'
line9 =  str(csvList[maxList[0]][1]) + str(csvList[maxList[0]][2]) + ',serial' + str(csvList[maxList[0]][4]) + ',', str(csvList[maxList[0]][5]) + ', with an average field test score of'+ str(maxList[1]) + '\n'

line10 = '\n'

#Color Histogram (using pretty print)
line11 ='Colors Histogram---' + '\n'
line12 = pprint.pformat(color_histogram_dict(csvList), indent=1, width=80, depth=None, compact=False, sort_dicts=True) #should return a string according to stackoverflow but I can't get it to work

#writing to txt file
#with open(filename2, 'w') as out_file:
    #out_file.writelines([line1, line2, line3, line4, line5, line6, line7, line8, line9, line10, line11, line12]) #I have no clue why line 9 is a tuple instead or string
