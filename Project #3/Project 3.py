import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

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

#A listOfList map out is list[rows][columns]
#This function makes a list out of one column in a list of list starting from default 0 due to not having a column row
#Parameters: list of lists made form a CSV file & the column number of that CSV file user wants to copy
#Return a list containing the value in a single column
def graph_column_to_List(listOfList, columnIndex):

    clist =[]
    #Range is 1 - len because the first row in the CSV file are labels and not data
    for i in range(len(listOfList)):
        clist.append(listOfList[i][columnIndex])

    return clist


#A listOfList map out is list[rows][columns]
#This function makes a list out of one column in a list of list starting from index 1 not default 0, uses boolean value to determine if pokemon is legendary
#Parameters: list of lists made form a CSV file & the column number of that CSV file user wants to copy, wheteve the list contain legendaries or none legendarys
#Return a list containing the value in a single column
def isLegendary_column_to_List(listOfList, columnIndex, isLegendary):

    llist =[]
    #Range is 1 - len because the first row in the CSV file are labels and not data
    for i in range(1,len(listOfList)):
        if listOfList[i][12] == isLegendary:
            #12 is column that contains boolean for Legendaries
            llist.append(listOfList[i][columnIndex])

    return llist


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


#A function that find the index of the pokemon with the highest particur stat in the list of list made by the pokemon.csv file
#Pre-condition: only work specifically for the project and pokemon.csv
#Return index of the pokemon the has the highest value of a certain stat(using column)
def highest_stat_pokemon_index(list_of_lists, col_num):

    int_stat_list = []
    stat_list = column_to_List(list_of_lists, col_num) #list of int of a particular stat

    for num in stat_list:
        int_stat_list.append(int(num))
    max_row_number = int_stat_list.index(max(int_stat_list))

    return max_row_number


#A function that find the index of the pokemon with the highest particur stat in the list of list made by the pokemon.csv file into legendries and non-legendries
#Pre-condition: only work specifically for the project and pokemon.csv
#Return index of the pokemon the has the highest value of a certain stat(using column)
def graph_highest_stat_pokemon_index(list_of_lists, col_num):

    int_stat_list = []
    stat_list = graph_column_to_List(list_of_lists, col_num) #list of int of a particular stat

    for num in stat_list:
        int_stat_list.append(int(num))
    max_row_number = int_stat_list.index(max(int_stat_list))

    return max_row_number


#A function that take a rownum and print that data contain in that row in the list of list made from pokemon.csv
#Pre-condition: only work specifically for the project and pokemon.csv
#No return: prints the pokemon's #, name, the stat choosen(col num), and legendary Status
def row_print(list_of_list, row_num, col_num):
    print('#:', list_of_list[row_num][0], 'Name:', list_of_list[row_num][1], list_of_list[0][col_num] + ':', list_of_list[row_num][col_num], 'Legendary?', list_of_list[row_num][12])

# A function that help splits the list of list created by Pokemon.csv into legendries and non-legendries
# Pre-condition: Only work with list of list created by Pokemon.csv
def split_list_of_list(list_of_list, isLegendary):

    new_list_of_list = []
    # Range is 1 - len because the first row in the CSV file are labels and not data
    for row in list_of_list:
        if row[12] == isLegendary:
            # 12 is column that contains boolean for Legendaries, label column exclude due to not = "True" or "False'
            new_list_of_list.append(row)

    return new_list_of_list

##################################################### MAIN APP ########################################################

#Read in that 'Pokemon.csv". Then use the csv_to_List function to make CSV file into list of Lists.
print('POKEMON.CSV LIST OF LIST')
print('------------------------')
csvList = csv_to_List('Pokemon.csv')
for row in csvList:
    print(*row)
print('')


########### Computing the average in each stat category of legendries & non-legendries ##########

#HP
HP_Legend_List = isLegendary_column_to_List(csvList, 5, 'True')
HP_Normie_List = isLegendary_column_to_List(csvList, 5, 'False')
Avg_HP_Legend = int_list_avg(HP_Legend_List)
Avg_HP_Normie = int_list_avg(HP_Normie_List)

#ATTACK
Attack_Legend_List = isLegendary_column_to_List(csvList, 6, 'True')
Attack_Normie_List = isLegendary_column_to_List(csvList, 6, 'False')
Avg_Attack_Legend = int_list_avg(Attack_Legend_List)
Avg_Attack_Normie = int_list_avg(Attack_Normie_List)

#DEFENSE
Defense_Legend_List = isLegendary_column_to_List(csvList, 7, 'True')
Defense_Normie_List = isLegendary_column_to_List(csvList, 7, 'False')
Avg_Defense_Legend = int_list_avg(Defense_Legend_List)
Avg_Defense_Normie = int_list_avg(Defense_Normie_List)

#SP Attack
SP_Attack_Legend_List = isLegendary_column_to_List(csvList, 8, 'True')
SP_Attack_Normie_List = isLegendary_column_to_List(csvList, 8, 'False')
Avg_SP_Attack_Legend = int_list_avg(SP_Attack_Legend_List)
Avg_SP_Attack_Normie = int_list_avg(SP_Attack_Normie_List)

#SP Defense
SP_Defense_Legend_List = isLegendary_column_to_List(csvList, 9, 'True')
SP_Defense_Normie_List = isLegendary_column_to_List(csvList, 9, 'False')
Avg_SP_Defense_Legend = int_list_avg(SP_Defense_Legend_List)
Avg_SP_Defense_Normie = int_list_avg(SP_Defense_Normie_List)

#Speed
Speed_Legend_List = isLegendary_column_to_List(csvList, 10, 'True')
Speed_Normie_List = isLegendary_column_to_List(csvList, 10, 'False')
Avg_Speed_Legend = int_list_avg(Speed_Legend_List)
Avg_Speed_Normie = int_list_avg(Speed_Normie_List)


#Printing the Comparision between the average stats of legendary Pokemon to Non-Legendary Pokemon
print('Is it true legendries have better stat averages than non-legendries?')
print('--------------------------------------------------------------------')
print('HP: ' + str(Avg_HP_Legend > Avg_HP_Normie))
print('Attack: ' + str(Avg_Attack_Legend > Avg_Attack_Normie))
print('Defense: ' + str(Avg_Defense_Legend > Avg_Defense_Normie))
print('SP Attack: ' + str(Avg_SP_Attack_Legend > Avg_SP_Attack_Normie))
print('SP Defense: ' + str(Avg_SP_Defense_Legend > Avg_SP_Defense_Normie))
print('Speed: ' + str(Avg_Speed_Legend > Avg_Speed_Normie))
print('')


########### Finding the pokemon with the highest value in each stat category ##########
HP_Poke = highest_stat_pokemon_index(csvList, 5) + 1  #Adding back label row
Attack_Poke = highest_stat_pokemon_index(csvList, 6) + 1  #Adding back label row
Defense_Poke = highest_stat_pokemon_index(csvList, 7) + 1  #Adding back label row
SP_Attack_Poke = highest_stat_pokemon_index(csvList, 8) + 1  #Adding back label row
Sp_Defense_Poke = highest_stat_pokemon_index(csvList, 9) + 1  #Adding back label row
Speed_Poke = highest_stat_pokemon_index(csvList, 10) + 1  #Adding back label row


#Printing the pokemon with the highest value in each stat category
print('Are the highest stat pokemon in each stat a legendary?')
print('------------------------------------------------------')
row_print(csvList, HP_Poke, 5)
row_print(csvList, Attack_Poke, 6)
row_print(csvList, Defense_Poke, 7)
row_print(csvList, SP_Attack_Poke, 8)
row_print(csvList, Sp_Defense_Poke, 9)
row_print(csvList, Speed_Poke, 10)
print('')


########### Finding the pokemon with the highest value in each stat category split legendries and non legendries ##########
leg_list = split_list_of_list(csvList, 'True')
norm_list = split_list_of_list(csvList, 'False')

########### test #########
#for row in leg_list:
#    print(*row)
#print('')

leg_HP_Poke = graph_highest_stat_pokemon_index(leg_list, 5)
leg_Attack_Poke = graph_highest_stat_pokemon_index(leg_list, 6)
leg_Defense_Poke = graph_highest_stat_pokemon_index(leg_list, 7)
leg_SP_Attack_Poke = graph_highest_stat_pokemon_index(leg_list, 8)
leg_SP_Defense_Poke = graph_highest_stat_pokemon_index(leg_list, 9)
leg_Speed_Poke = graph_highest_stat_pokemon_index(leg_list, 10)

norm_HP_Poke = graph_highest_stat_pokemon_index(norm_list, 5)
norm_Attack_Poke = graph_highest_stat_pokemon_index(norm_list, 6)
norm_Defense_Poke = graph_highest_stat_pokemon_index(norm_list, 7)
norm_SP_Attack_Poke = graph_highest_stat_pokemon_index(norm_list, 8)
norm_SP_Defense_Poke = graph_highest_stat_pokemon_index(norm_list, 9)
norm_Speed_Poke = graph_highest_stat_pokemon_index(norm_list, 10)

#Making List for Histogram
X = ['HP','Attack','Defense','SP. Attack','SP. Defense', 'Speed']
Y = []
Z = []

Y.append(int(leg_list[leg_HP_Poke][5]))
Y.append(int(leg_list[leg_Attack_Poke][6]))
Y.append(int(leg_list[leg_Defense_Poke][7]))
Y.append(int(leg_list[leg_SP_Attack_Poke][8]))
Y.append(int(leg_list[leg_SP_Defense_Poke][9]))
Y.append(int(leg_list[leg_Speed_Poke][10]))

Z.append(int(norm_list[norm_HP_Poke][5]))
Z.append(int(norm_list[norm_Attack_Poke][6]))
Z.append(int(norm_list[norm_Defense_Poke][7]))
Z.append(int(norm_list[norm_SP_Attack_Poke][8]))
Z.append(int(norm_list[norm_SP_Defense_Poke][9]))
Z.append(int(norm_list[norm_Speed_Poke][10]))

print(Y)
print(Z)

#Plotting Highest Stat Category legendries and Non Legendries to observe the diffence between the best
fig, ax = plt.subplots()
df = pd.DataFrame(np.c_[Y,Z], index=X)
df.plot.bar(ax=ax, title='Highest Stat Pokemon Comparision')
ax.legend(["Legendary", "Non-Legendary"])

plt.show()

