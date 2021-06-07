import csv
import os

class BudgetItem():

    def __init__(self, **kwargs):
        self.category = kwargs['Category']
        self.budget = max(0, int(kwargs['Budget']))
        self.expense = max(0, int(kwargs['Expense']))

    @classmethod
    def read_budget(self):
        budget_items = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/test_budget.csv")

        with open(path) as csvfile:
            dict_reader = csv.DictReader(csvfile)
            for line in dict_reader:
                budget_items.append(BudgetItem(**line))

        return budget_items
    
    def __str__(self):
        return f"{self.category}\t  {self.budget}\t  {self.expense}"

    def calculate_expense_income_ratio(self, income):
        
        return "{:.2f}".format(self.expense / income)
