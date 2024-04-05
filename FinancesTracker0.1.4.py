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
class saveDataCommands:
    def __init__(self, transaction_instance):
        self.transaction_instance = transaction_instance
        
    def saveSpendingReceipt(self):
        date = dt.date(self.transaction_instance.YYYY, self.transaction_instance.MM, self.transaction_instance.DD)
        
        spendingData = {
            'Date': [str(date)],
            'Price': [self.transaction_instance.QTY],
            'Name': [self.transaction_instance.name],
            'Category of Revenue': [self.transaction_instance.category],
            'Source of Revenue': [self.transaction_instance.business]}
        
        df = pd.DataFrame(spendingData)
        filepath = str(date)+str(self.transaction_instance.business)+'spendingData.csv'
        df.to_csv(filepath)

    def saveRevenueReceipt(self):
        date = dt.date(self.transaction_instance.YYYY, self.transaction_instance.MM, self.transaction_instance.DD)
        
        revenueData = {
            'Date': [str(date)],
            'Price': [self.transaction_instance.QTY],
            'Name': [self.transaction_instance.name],
            'Category of Revenue': [self.transaction_instance.category],
            'Source of Revenue': [self.transaction_instance.business]}
        
        df = pd.DataFrame(revenueData)
        filepath = str(date)+str(self.transaction_instance.business)+'revenueData.csv'
        df.to_csv(filepath)

transaction_instance = Revenue("Tea", "Teashop", 1000, "Food & Drink", 2024, 3, 31)
print(transaction_instance.revenueQTYDate)

save_instance = saveDataCommands(transaction_instance)
save_instance.saveRevenueReceipt()