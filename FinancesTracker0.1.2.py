import pandas as pd
import datetime as dt



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
        self.spendingQTYDate[date] = QTY
        
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
        self.revenueQTYDate[date] = QTY
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

class saveDataCommands(Profits, Spending, Revenue):
    def __init__(self, name, business, QTY, category, YYYY, MM, DD):
        Profits.__init__(self, name) 
        Spending.__init__(self, name, business, QTY, category, YYYY, MM, DD )  
        Revenue.__init__(self, name)
        
    def saveSpending(self, name, business, QTY, category, YYYY, MM, DD):
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
        
    def saveRevenue(self, name, business, QTY, category, YYYY, MM, DD):
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