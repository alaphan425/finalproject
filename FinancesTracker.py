import pandas as pd
import os
import datetime as dt
import matplotlib as plt
import tkinter as tk


"""Create a class that takes the name of the expense (ie bill, ingredients,
 machinery, etc), the business the expense was spent on, the quantity of the 
expense, the year, the month, and the day. Create datetime objects with the 
year, month, and day in the ISO 8601 date format.
"""
class Expense:
    def __init__(self, name, business, QTY, category, YYYY, MM, DD):
        
        # Initialization of variables
        self.name = name
        self.business = business
        self.QTY = QTY
        self.category = category
        self.YYYY = YYYY
        self.MM = MM
        self.DD = DD
        
        
        # Create a dictionary to assign spending dates and values.
        self.expenseQTYDate = {}
        
        # Define date variable to use with the datetime library.
        date = dt.date(YYYY, MM, DD)
        
        # Associate spending amount with ISO 8601 date format.
        self.expenseQTYDate[date.isoformat()] = QTY


"""Create a class that takes the name of the revenue (ie product sales, tax
rebate, interest, etc), the business that was the source of the revenue, the 
quantity of the expense, the year, the month, and the day. Create datetime
objects with the year, month, and day in the ISO 8601 date format.
"""
class Revenue:
    def __init__(self, name, business, QTY, category, YYYY, MM, DD):

        # Initialization of variables
        self.name = name
        self.business = business
        self.QTY = QTY
        self.category = category
        self.YYYY = YYYY
        self.MM = MM
        self.DD = DD
        
        # Create a dictionary to assign revenue dates and values.
        self.revenueQTYDate = {}
        
        # Define date variable to use with the datetime library.
        date = dt.date(YYYY, MM, DD)
        
        # Associate spending amount with date
        self.revenueQTYDate[date.isoformat()] = QTY
        
"""Create a class which takes Revenue or Expense objects as their input and
saves the data to .csv files in different ways.
"""
class SaveDataCommands:
    def __init__(self, transactionInstance):
        # Initialization of variables
        self.transactionInstance = transactionInstance
    
    """Method to save attributes of expense instances to .csv files"""
    def save_expenses_receipt(self):
        # Use the object's year, month, and day attributes to make dt objects
        date = dt.date(self.transactionInstance.YYYY,
                       self.transactionInstance.MM,
                       self.transactionInstance.DD)
        
        # Create a dictionary with the information of the expense object
        expenseData = {
                        'Date': [str(date.isoformat())],
                        'Price': [self.transactionInstance.QTY],
                        'Expense Name': [self.transactionInstance.name],
                        'Expense Category': [self.transactionInstance.category],
                        'Expense Source': [self.transactionInstance.business]
                        }
        
        # Use the DataFrame function to use expenseData as a dataframe 
        df = pd.DataFrame(expenseData)
        
        # Name a csv file with the transaction category, date, and whatever business
        # it belongs to, and then write the dataframe to that file. Have no index since it's
        # only one entry
        filepath = str(self.transactionInstance.category)+str(date)+str(self.transactionInstance.business)+'ExpenseData.csv'
        df.to_csv(filepath, index = False)
    
    """Method to save attributes of revenue instances to .csv files"""
    def save_revenue_recepit(self):
        # Use the object's year, month, and day attributes to make dt objects
        date = dt.date(self.transactionInstance.YYYY,
                       self.transactionInstance.MM,
                       self.transactionInstance.DD)
        
        # Create a dictionary with the information of the revenue object
        revenueData ={
                      'Date': [str(date.isoformat())],
                      'Price': [self.transactionInstance.QTY],
                      'Revenue Name': [self.transactionInstance.name],
                      'Revenue Category': [self.transactionInstance.category],
                      'Revenue Source': [self.transactionInstance.business]
                      }
        
        # Use the DataFrame function to use revenueData as a dataframe structure
        df = pd.DataFrame(revenueData)
        
        # Name a csv file with the transaction category, date, and whatever business
        # it belongs to, and then write the dataframe to that file. Have no index since it's
        # only one entry.
        filepath = str(self.transactionInstance.category)+str(date)+str(self.transactionInstance.business)+'RevenueData.csv'
        df.to_csv(filepath, index = False)
    
    """Method to write expense data to a permanent log in chronological order."""
    def write_expense_to_log(self):
        # Use the object's year, month, and day attributes to make dt objects
        date = dt.date(self.transactionInstance.YYYY,
                       self.transactionInstance.MM,
                       self.transactionInstance.DD)
        
        # Create a dictionary with the information of the expense object
        expenseLogData ={
                        'Date': [str(date.isoformat())],
                        'Price': [self.transactionInstance.QTY],
                        'Expense Name': [self.transactionInstance.name],
                        'Expense Category': [self.transactionInstance.category],
                        'Expense Source': [self.transactionInstance.business]
                        }
        
        # Use the DataFrame function to use expenseDf as a dataframe structure
        expenseDf = pd.DataFrame(expenseLogData)
        
        # Name a csv file with the transaction category, date, and whatever business
        # it belongs to.
        filepath = str(self.transactionInstance.business)+"ExpensesLogbook.csv"
        
        # If the file filepath checked before is not a file, write the dataframe
        # to a new csv file with that name. Create the files with no index since we want
        # the files sorted chronologically.
        if not os.path.isfile(filepath):
            expenseDf.to_csv(filepath, index = False) 
        else:
            # Read the current filepath csv file into a holder dataframe named currentDf
            currentDf = pd.read_csv(filepath)
            
            # Create a new dataframe called dateSortedDf and make it the concatated 
            # dataFrame from the 0th axis of currentDf and expenseDf, and make ignore_index
            # = True to ignore the index of the previous file, and make new indexes.
            dateSortedDf = pd.concat([currentDf, expenseDf], ignore_index=True)
            
            # Sort dateSortedDf by the 'Date' column. Since these are in ISO 8601,
            # we can just sort them. Write them to the filepath variable and have no
            # index on them again.
            dateSortedDf = dateSortedDf.sort_values(by='Date')
            dateSortedDf.to_csv(filepath, index=False)
        
    """Method to write revenue data to a permanent log in chronological order."""
    def write_revenue_to_log(self):
        # Use the object's year, month, and day attributes to make dt objects
        date = dt.date(self.transactionInstance.YYYY,
                       self.transactionInstance.MM,
                       self.transactionInstance.DD)
        
        # Create a dictionary with the information of the revenue object
        revenueLogData ={
                         'Date': [str(date.isoformat())],
                         'Price': [self.transactionInstance.QTY],
                         'Revenue Name': [self.transactionInstance.name],
                         'Revenue Category': [self.transactionInstance.category],
                         'Revenue Source': [self.transactionInstance.business]
                        }
        
        # Use the DataFrame function to use revenueData as a dataframe structure
        revenueDf = pd.DataFrame(revenueLogData)
        
        # Name a csv file with the transaction category, date, and whatever business
        # it belongs to.
        filepath = str(self.transactionInstance.business)+"RevenueLogbook.csv"
        
        # If the file filepath checked before is not a file, write the dataframe
        # to a new csv file with that name. Create the files with no index since we want
        # the files sorted chronologically.
        if not os.path.isfile(filepath):
            revenueDf.to_csv(filepath, index = False)
        else:
            # Read the current filepath csv file into a holder dataframe named currentDf
            currentDf = pd.read_csv(filepath)
            
            # Create a new dataframe called dateSortedDf and make it the concatated 
            # dataFrame from the 0th axis of currentDf and expenseDf, and make ignore_index
            # = True to ignore the index of the previous file, and make new indexes.
            dateSortedDf = pd.concat([currentDf, revenueDf], ignore_index=True)
            
            # Sort dateSortedDf by the 'Date' column. Since these are in ISO 8601,
            # we can just sort them. Write them to the filepath variable and have no
            # index on them again.
            dateSortedDf = dateSortedDf.sort_values(by='Date')
            dateSortedDf.to_csv(filepath, index=False)
            
"""Class to take the business name attribute of transaction objects
and then at each input of a new datapoint in the respective business' revenue
or expense logbook, recalculates the profit earned on that day for that business.
"""
class Profits:
    def __init__(self, transactionInstance):
        # Initialize transactionInstance variable
            self.transactionInstance = transactionInstance
    """Method to calculate the profits of every day by subtracting the revenue
    from the expenditure. If there is only revenue or expenditure for one day,
    that value is the net profit. function should be called every time new
    a transaction instance is added to the log.
    """
    def calculate_profits(self):
        
        # Read revenue and expense data from their respective csv files
        revenueDf = pd.read_csv(str(self.transactionInstance.business)
                                +"RevenueLogbook.csv", parse_dates=['Date']
                                )
        
        expenseDf = pd.read_csv(str(self.transactionInstance.business)
                                +"ExpensesLogbook.csv", parse_dates=['Date']
                                )
        # Convert 'Date' column to datetime format because read_csv reads as a
        # string
        revenueDf['Date'] = pd.to_datetime(revenueDf['Date'])
        expenseDf['Date'] = pd.to_datetime(expenseDf['Date'])

        # Fill missing values in 'Revenue Source' and 'Price' columns with with
        # zero and the name of the business.
        revenueDf['Revenue Source'].fillna(self.transactionInstance.business, inplace=True)
        revenueDf['Price'].fillna(0, inplace=True)
        
        expenseDf['Expense Source'].fillna(self.transactionInstance.business, inplace=True)
        expenseDf['Price'].fillna(0, inplace=True)

        # Merge the revenue and expense dataframes based on their date.
        profitsDf = pd.merge(revenueDf, expenseDf, on='Date', how='outer')
        
        # Say that the profits column is the difference between the Price_x 
        # (revenueDf), and Price_y (expenseDf).
        profitsDf['Profit'] = profitsDf['Price_x'] - profitsDf['Price_y']
        
        # Create a dictionary for profits data based on the date, name of the
        # business and calculated amount of profit
        profitData = {
            'Date': profitsDf['Date'],
            'Business': profitsDf['Expense Source'],
            'Profit': profitsDf['Profit']
                      }
        # Create a new dataframe with the ProfitsData dictionary
        profitsDf = pd.DataFrame(profitData)
        
        # Create a filepath with the name of the Profits data csv.
        filepath = str(self.transactionInstance.business)+"Profits.csv"
        
        # Check if the filepath exists, if it does write it there with no index
        # numbers.
        if not os.path.isfile(filepath):
            profitsDf.to_csv(filepath, index = False)
        else:
            # Read the existing filepath, define it as a dataframe called
            # currentDf, and read the dates column as datetime objects
            currentDf = pd.read_csv(filepath, parse_dates=['Date'])
            
            # Create a new dataframe called dateSortedDf and make it the concatated 
            # dataFrame from the 0th axis of currentDf and profitsDf, and make ignore_index
            # = True to ignore the index of the previous file, and make new indexes.
            dateSortedDf = pd.concat([currentDf, profitsDf], ignore_index=True)
            
            # Sort the values by the date and write them to filepath with no
            # index numbers.
            dateSortedDf = dateSortedDf.sort_values(by='Date')
            dateSortedDf.to_csv(filepath, index=False)
            
DataCommands = SaveDataCommands
profits = Profits

revenueInstance = Revenue("Tea", "Teashop", 1500, "Beverage", 2024, 4, 15)
expenseInstance = Expense("Tea leaves", "Teashop", 300, "Ingredients", 2024, 3, 15)

DataCommands = SaveDataCommands(revenueInstance)
DataCommands.write_revenue_to_log()
DataCommands = SaveDataCommands(expenseInstance)
DataCommands.write_expense_to_log()

profitsCalculate = Profits(revenueInstance)
profitsCalculate.calculate_profits()