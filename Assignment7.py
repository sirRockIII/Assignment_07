# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 21:09:47 2022

@author: Emeka
"""

#------------------------------------------#
# Title: Assignment06.py
# Desc: Working with classes and functions.
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# COsuji, 2022-Aug-14, Restructured script by adding functions for data addition and deletion
# COsuji, 2022-Aug-14, Restructured script by adding functions for writing to file and other functionalities
#------------------------------------------#

# -- DATA -- #
strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dicRow = {}  # list of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object


# -- PROCESSING -- #
class DataProcessor:
    """Processing the addition and deletion data """
    
   
    @staticmethod
    def process_adding_data(iD, title, artist, table):
        """Function to manage data addtion to table

        Adds user input data to 2D table (list of dicts)

        Args:
            iD (integer): ID entry from user input
            Title (string): CD title string name entry from user input
            Artist (string): Artist title string name entry from user input
            Table (list): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
            
        dicRow = {'ID': iD, 'Title': title, 'Artist': artist}
        table.append(dicRow)
        
    @staticmethod    
    def process_deleting_data(intIDDel, table ):
        """Function to manage data deletion to table

        delets data entries based on user ID number data from 2D table (list of dicts)

        Args:
            intIDDel (integer): user requested data entry ID to be deleted. 
            table  (list): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        
        intRowNr = -1
        blnCDRemoved = False
        for row in table:
            intRowNr += 1
            if row['ID'] == intIDDel:
                del lstTbl[intRowNr]
                blnCDRemoved = True
                break
        if blnCDRemoved:
            print('The CD was removed')
        else:
            print('Could not find this CD!')
        
    
    


class FileProcessor:
    """Processing the data to and from text file"""

    @staticmethod
    def read_file(file_name, table):
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        table.clear()  # this clears existing data and allows to load data from file
        try:
            objFile = open(file_name, 'r')
        except FileNotFoundError as e:
            print("An error occured when attmepitng to read in currently saved inventory from file")
            print("Build in error info")
            print(type(e), e ,e.__doc__, sep = '\n')
        else: 
            for line in objFile:
                data = line.strip().split(',')
                dicRow = {'ID': int(data[0]), 'Title': data[1], 'Artist': data[2]}
                table.append(dicRow)
            objFile.close()
       
            

    @staticmethod
    def write_file(file_name, table):
        """Function to manage data emisson from a list of dictionaries to a file
    
        Reads the data from a 2D table (list of dicts) to a file identified by file_name 
    
        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime
    
        Returns:
            None.
        """
        try:
            objFile = open(file_name, 'w')
        except:
            print('An error occured when attempting to write data to the file')
        else:
            for row in table:
                lstValues = list(row.values())
                lstValues[0] = str(lstValues[0])
                objFile.write(','.join(lstValues) + '\n')
            objFile.close()
        finally:
            objFile.close()
            


# -- PRESENTATION (Input/Output) -- #

class IO:
    """Handling Input / Output"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print('{}\t {} (by:{})'.format(*row.values()))
        print('======================================')
        
    
    @staticmethod
    def add_inventory():
        """Requests user data input for data entry


        Args:
            None.

        Returns:
            strID (integer): ID entry from user input
            strTitle (string): CD title string name entry from user input
            strArtist (string): Artist title string name entry from user input

        """
        strID = input('Enter ID: ').strip()
        strTitle = input('What is the CD\'s title? ').strip()
        stArtist = input('What is the Artist\'s name? ').strip()
        
            
        
        return strID, strTitle, stArtist
    
    
   

# 1. When program starts, read in the currently saved Inventory
FileProcessor.read_file(strFileName, lstTbl)

# 2. start main loop
while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()

    # 3. Process menu selection
    # 3.1 process exit first
    if strChoice == 'x':
        break 
    # 3.2 process load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            FileProcessor.read_file(strFileName, lstTbl)
            IO.show_inventory(lstTbl)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.3 process add a CD
    elif strChoice == 'a':
        # 3.3.1 Ask user for new ID, CD Title and Artist
      
        try:
            inputted_Data = IO.add_inventory()
            intNum = int(inputted_Data[0])
        except ValueError as e:
            print("Please enter a number as the inventory ID")
            print("Build in error info")
            print(type(e), e ,e.__doc__, sep = '\n')
            continue
                
            
            

        # 3.3.2 Add item to the table
        DataProcessor.process_adding_data(inputted_Data[0], inputted_Data[1], inputted_Data[2], lstTbl)
        
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.4 process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.5 process delete a CD
    elif strChoice == 'd':
        # 3.5.1 get Userinput for which CD to delete
        # 3.5.1.1 display Inventory to user
        IO.show_inventory(lstTbl)
        # 3.5.1.2 ask user which ID to remove
        try:
            intIDDel = int(input('Which ID would you like to delete? ').strip())
        except ValueError as e:
            print("Please enter a number as the inventory ID")
            print("Build in error info")
            print(type(e), e ,e.__doc__, sep = '\n')
            continue
            
        # 3.5.2 search thru table and delete CD
       
        DataProcessor.process_deleting_data(intIDDel, lstTbl)
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.6 process save inventory to file
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstTbl)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y':
            # 3.6.2.1 save data
          
            FileProcessor.write_file(strFileName, lstTbl)
            
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')




