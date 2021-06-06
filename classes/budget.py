# Budget instances are stored as a list of dictionaries
# Each element of the list of Budget instances is stored
# in the format 
# "Category": category_name
# "Budget": budgeted_amount
# "Expense": current_expenditures

import csv
import os

class Budget():

    def __init__(self, name):
        self.name = name
        print(f"{self.name}'s budget\n------------------")
        self.budget = self.read_budget()
        pass

    def read_budget(self):
        budget_items = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/test_budget.csv")

        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                budget_items.append(row)
                budget_items[-1]['Budget'] = int(budget_items[-1]['Budget'])
                budget_items[-1]['Expense'] = int(budget_items[-1]['Expense'])

        return budget_items
    
    def print_budget(self):
        if len(self.budget) == 0:
            return
        
        header = "  "
        budget_keys = list(self.budget[0].keys())
        print(header.join(budget_keys))
        print("----------------------------")

        for budget_item in self.budget:
        #    print(budget_item)
            for key in budget_item:
                print(budget_item[key], end="  ")

            print("\n")    

    def add_transaction(self, category, amount):

        for budget_item in self.budget:
            if budget_item['Category'] == category:
                # updates expense amount, if the new expense amount would be less than zero, round to zero
                budget_item['Expense'] = max(0, budget_item["Expense"] + amount)
                return

        print("Error: unable to process transaction, category not in budget")

    def change_budget_amount(self, category, amount):
        
        for budget_item in self.budget:
            if budget_item['Category'] == category:
                # updates category amount, if the new budget amount is less than zero, round to zero
                budget_item['Budget'] = max(0, amount)
                return

        print("Error: unable to update budget amount, category not in budget")

    def add_budget_category(self, new_category,new_budget_amount):

        self.budget.append({"Category": new_category, "Budget": max(0, new_budget_amount), "Expense": 0})
        print(self.budget[-1])

    def remove_budget_category(self, category_to_remove):
        for index, budget_item in enumerate(self.budget):
            if budget_item['Category'] == category_to_remove:
                self.budget.pop(index)
                return

        print("Error: unable to remove budget category, category not in budget")