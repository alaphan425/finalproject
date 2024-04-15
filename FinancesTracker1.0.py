import pandas as pd
import os
import datetime as dt
import matplotlib as mpl
import tkinter as tk

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
        
        # Define date variable to use dynamically with the datetime library.
        date = dt.date(YYYY, MM, DD)
        
        # Associate spending amount with date
        self.expenseQTYDate[date.isoformat()] = QTY



class Revenue:
    def __init__(self, name, business, QTY, category, YYYY, MM, DD):
        # Initialization
        self.name = name
        self.business = business
        self.QTY = QTY
        self.category = category
        self.YYYY = YYYY
        self.MM = MM
        self.DD = DD
        
        # Create a dictionary to assign revenue dates and values. 
        self.revenueQTYDate = {}
        
        # Define date variable to use dynamically with the datetime library.
        date = dt.date(YYYY, MM, DD)
        
        # Associate revenue amount with date
        self.revenueQTYDate[date.isoformat()] = QTY

class SaveDataCommands:
    def __init__(self, transactionInstance):
        self.transactionInstance = transactionInstance
        
    def save_expenses_receipt(self):
        date = dt.date(self.transactionInstance.YYYY, self.transactionInstance.MM, self.transactionInstance.DD)
        
        expenseData = {
            'Date': [str(date.isoformat())],
            'Price': [self.transactionInstance.QTY],
            'Expense Name': [self.transactionInstance.name],
            'Expense Category': [self.transactionInstance.category],
            'Expense Source': [self.transactionInstance.business]}
        
        df = pd.DataFrame(expenseData)
        filepath = str(date)+str(self.transactionInstance.business)+'expenseData.csv'
        df.to_csv(filepath)

    def save_revenue_recepit(self):
        date = dt.date(self.transactionInstance.YYYY, self.transactionInstance.MM, self.transactionInstance.DD)
        
        revenueData = {
            'Date': [str(date.isoformat())],
            'Price': [self.transactionInstance.QTY],
            'Revenue Name': [self.transactionInstance.name],
            'Revenue Category': [self.transactionInstance.category],
            'Revenue Source': [self.transactionInstance.business]}
        
        df = pd.DataFrame(revenueData)
        filepath = str(date)+str(self.transactionInstance.business)+'RevenueData.csv'
        df.to_csv(filepath)
        
    def write_expense_to_log(self):
        date = dt.date(self.transactionInstance.YYYY, self.transactionInstance.MM, self.transactionInstance.DD)
                
        expenseLogData = {
            'Date': [str(date.isoformat())],
            'Price': [self.transactionInstance.QTY],
            'Expense Name': [self.transactionInstance.name],
            'Expense Category': [self.transactionInstance.category],
            'Expense Source': [self.transactionInstance.business]}
        
        expenseDf = pd.DataFrame(expenseLogData)
        filepath = str(self.transactionInstance.business)+"ExpensesLogbook.csv"
        
        if os.path.isfile(filepath) == False:
            expenseDf.to_csv(filepath, index = False)
        else:
            currentDf = pd.read_csv(filepath)
            dateSortedDf = pd.concat([currentDf, expenseDf], ignore_index=True)
            dateSortedDf = dateSortedDf.sort_values(by='Date')
            dateSortedDf.to_csv(filepath, index=False)
        

    def write_revenue_to_log(self):
        date = dt.date(self.transactionInstance.YYYY, self.transactionInstance.MM, self.transactionInstance.DD)
        
        revenueLogData = {
            'Date': [str(date.isoformat())],
            'Price': [self.transactionInstance.QTY],
            'Revenue Name': [self.transactionInstance.name],
            'Revenue Category': [self.transactionInstance.category],
            'Revenue Source': [self.transactionInstance.business]}
        
        revenueDf = pd.DataFrame(revenueLogData)
        filepath = str(self.transactionInstance.business)+"RevenueLogbook.csv"
        
        if os.path.isfile(filepath) == False:
            revenueDf.to_csv(filepath, index = False)
        else:
            currentDf = pd.read_csv(filepath)
            dateSortedDf = pd.concat([currentDf, revenueDf], ignore_index=True)
            dateSortedDf = dateSortedDf.sort_values(by='Date')
            dateSortedDf.to_csv(filepath, index=False)
            
            
# Create a class able to calculate profits that inherits from the Spending and
# Revenue classes
class Profits:
    def __init__(self, transactionInstance):
            self.transactionInstance = transactionInstance
            
    def calculate_profits(self):
        revenueDf = pd.read_csv(str(self.transactionInstance.business)+"RevenueLogbook.csv", parse_dates=['Date'])
        expenseDf = pd.read_csv(str(self.transactionInstance.business)+"ExpensesLogbook.csv", parse_dates=['Date'])
        
        revenueDf = revenueDf.dropna(subset=['Date'])
        expenseDf = expenseDf.dropna(subset=['Date'])
        
        revenueDf['Date'] = pd.to_datetime(revenueDf['Date'])
        expenseDf['Date'] = pd.to_datetime(expenseDf['Date'])
        
        allDates = pd.date_range(start=min(revenueDf['Date'].min(), expenseDf['Date'].min()), end=max(revenueDf['Date'].max(), expenseDf['Date'].max()))
       
        dateDf = pd.DataFrame(allDates, columns=['Date'])
        
        revenueDf = pd.merge(dateDf, revenueDf, on='Date', how='left')
        expenseDf = pd.merge(dateDf, expenseDf, on='Date', how='left')
        
        revenueDf['Revenue Source'].fillna(self.transactionInstance.business, inplace=True)
        revenueDf['Price'].fillna(0, inplace=True)
        expenseDf['Expense Source'].fillna(self.transactionInstance.business, inplace=True)
        expenseDf['Price'].fillna(0, inplace=True)

        profitsDf = pd.merge(revenueDf, expenseDf, on='Date', how='outer')
        profitsDf['Profit'] = profitsDf['Price_x'] - profitsDf['Price_y']
        
        profitData = {
            'Date': profitsDf['Date'],
            'Business': profitsDf['Expense Source'],
            'Profit': profitsDf['Profit']}
        
        profitsDf = pd.DataFrame(profitData)
        filepath = str(self.transactionInstance.business)+"Profits.csv"
        
        if os.path.isfile(filepath) == False:
            profitsDf.to_csv(filepath, index = False)
        else:
            currentDf = pd.read_csv(filepath, parse_dates=['Date'])
            dateSortedDf = pd.concat([currentDf, profitsDf], ignore_index=True)
            dateSortedDf = dateSortedDf.sort_values(by='Date')
            dateSortedDf.to_csv(filepath, index=False)

revenueInstance = Revenue("Tea", "Teashop", 1000, "Beverage", 2024, 5, 16)
expenseInstance = Expense("Tea Leaves", "Teashop", 200, "Ingredients", 2028, 7, 17)

revenue_save = SaveDataCommands(revenueInstance)
expense_save = SaveDataCommands(expenseInstance)

revenue_save.write_revenue_to_log()
expense_save.write_expense_to_log()

profitsInstance = Profits(revenueInstance)

profitsInstance.calculate_profits()