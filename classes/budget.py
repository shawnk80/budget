# Budget instances are stored as a list of dictionaries
# Each element of the list of Budget instances is stored
# in the format 
# "Category": category_name
# "Budget": budgeted_amount
# "Expense": current_expenditures

import csv
import os
from classes.budget_item import BudgetItem
class Budget():

    def __init__(self, name):
        self.name = name
        print(f"{self.name}'s budget\n------------------")
        self.income = self.read_income()
        self.budget = BudgetItem.read_budget()
        pass
    
    def read_income(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/income.csv")

        with open(path) as csvfile:
            dict_reader = csv.DictReader(csvfile)
            for line in dict_reader:
                return max(0, int(line['Income']))

    def print_budget(self):
        print("Category  Budget  Expense  % Income")

        for category in self.budget:
            print(category.expense, self.income)
            expense_ratio = category.calculate_expense_income_ratio(self.income)
            print(str(expense_ratio))

    def add_transaction(self, category, amount):
        pass
        # for budget_item in self.budget:
        #     if budget_item['Category'] == category:
        #         # updates expense amount, if the new expense amount would be less than zero, round to zero
        #         budget_item['Expense'] = max(0, budget_item["Expense"] + amount)
        #         return

        # print("Error: unable to process transaction, category not in budget")

    def change_budget_amount(self, category, amount):
        pass
        # for budget_item in self.budget:
        #     if budget_item['Category'] == category:
        #         # updates category amount, if the new budget amount is less than zero, round to zero
        #         budget_item['Budget'] = max(0, amount)
        #         return

        # print("Error: unable to update budget amount, category not in budget")

    def add_budget_category(self, new_category,new_budget_amount):
        pass
        # self.budget.append({"Category": new_category, "Budget": max(0, new_budget_amount), "Expense": 0})
        # print(self.budget[-1])

    def remove_budget_category(self, category_to_remove):
        pass
        # for index, budget_item in enumerate(self.budget):
        #     if budget_item['Category'] == category_to_remove:
        #         self.budget.pop(index)
        #         return

        # print("Error: unable to remove budget category, category not in budget")