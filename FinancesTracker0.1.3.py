import pandas as pd
import os
import datetime as dt
import matplotlib as mpl
import tkinter as tk

class Spending:
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
        self.spendingQTYDate = {}
        
        # Define date variable to use dynamically with the datetime library.
        date = dt.date(YYYY, MM, DD)
        
        # Associate spending amount with date
        self.spendingQTYDate[date.isoformat()] = QTY
        
    def spendingReceit(self, name, business, QTY, category):
        placeholder = name
            
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
        
    def revenueReceipt(self, name, business, QTY, category):
        placeholder = name

# Create a class able to calculate profits that inherits from the Spending and
# Revenue classes
class Profits(Spending, Revenue):
    def __init__(self):
        
        # Initialize date-profit dictionary and profit amount counter.
        self.datedProfits = {}
        profit = 0
        
        # Subtract the Revenue values from the Spending values for every pair
        # that contains the same key, and assign the new value to the mutual date
        # and put the profit-date pair into the dictionary.
        for date in set(Revenue.revenueQTYDate.keys()) & set(Spending.spendingQTYDate.keys()):
             profit = float(Revenue.revenueQTYDate[date]) - float(Spending.spendingQTYDate[date])
             self.datedProfits[date] = profit
        return date

class saveDataCommands(Spending, Revenue):
    def __init__(self, name, business, QTY, category, YYYY, MM, DD):
        Spending.__init__(self, name, business, QTY, category, YYYY, MM, DD )  
        Revenue.__init__(self, name, business, QTY, category, YYYY, MM, DD)
        
    def saveSpendingReceipt(self, name, business, QTY, category, YYYY, MM, DD):
        Spending.name = name
        Spending.business = business
        Spending.QTY = QTY
        Spending.category = category
        Spending.YYYY = YYYY
        Spending.MM = MM
        Spending.DD = DD
    
        date = dt.date(YYYY, MM, DD)
        
        spendingData = {
        'Date': [str(date)],
        'Price': [QTY],
        'Name': [name],
        'Category of Revenue': [category],
        'Source of Revenue': [business]}
        df = pd.DataFrame(spendingData)
        filepath ='spendingData.csv'
        df.to_csv(str(filepath))
        
    def saveRevenueReceipt(self, name, business, QTY, category, YYYY, MM, DD):
        Revenue.name = name
        Revenue.business = business
        Revenue.QTY = QTY
        Revenue.category = category
        Revenue.YYYY = YYYY
        Revenue.MM = MM
        Revenue.DD = DD
        
        date = dt.date(YYYY, MM, DD)
            
        spendingData = {
        'Date': [str(date)],
        'Price': [QTY],
        'Name': [name],
        'Category of Revenue': [category],
        'Source of Revenue': [business]}
        df = pd.DataFrame(spendingData)
        filepath = 'revenueData.csv'
        df.to_csv(str(filepath))
    
revenue_instance = Revenue("Sales", "Teashop", 10000, "xyz", 2024, 3, 31)
print(revenue_instance.revenueQTYDate)

save_instance = saveDataCommands("Sales", "Teashop", 10000, "xyz", 2024, 3, 31)
save_instance.saveRevenueReceipt("Sales", "Teashop", 10000, "xyz", 2024, 3, 31)
print(os.getcwd())