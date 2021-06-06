class Interface():

    def run(self):

        while True:
            user_input = self.menu()
            print(user_input)
            break

    def menu(self):
        keyboard_input = input("1. View Budget\n2. Add Transaction\n3. Delete Transaction\n4. Change Budgeted Amount\n5. Add Budget Category\n6. Remove Budget Category\n7. Quit\n")
        return keyboard_input
