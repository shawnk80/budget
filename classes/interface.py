from classes.budget import Budget

class Interface():

    budget = Budget("John")

    def run(self):

        while True:
            user_input = self.menu()
            
            if user_input == '1':
                self.view_budget()
            elif user_input == '2':
                self.add_transaction()
            elif user_input == '3':
                self.change_budget_amount()
            elif user_input == '4':
                self.add_budget_category()
            elif user_input == '5':
                self.remove_budget_category()
            elif user_input == '6':
                break

    def menu(self):
        keyboard_input = input("1. View Budget\n2. Add Transaction\n3. Change Budgeted Amount\n4. Add Budget Category\n5. Remove Budget Category\n6. Quit\n> ")
        return keyboard_input

    def view_budget(self):
        self.budget.print_budget()

    def add_transaction(self):
        category = input("Enter transaction category\n> ")
        amount = input("Enter transaction amount\n> ")
        self.budget.add_transaction(category, int(amount))

    def change_budget_amount(self):
        category = input("Enter budget category\n >")
        amount = input("Enter new budget amount\n> ")
        self.budget.change_budget_amount(category, int(amount))

    def add_budget_category(self):
        new_category = input("Enter new budget category\n >")
        new_budget_amount = input("Enter new budget amount\n> ")
        self.budget.add_budget_category(new_category, int(new_budget_amount))

    def remove_budget_category(self):
        category_to_remove = input("Enter budget category to delete\n> ")
        self.budget.remove_budget_category(category_to_remove)