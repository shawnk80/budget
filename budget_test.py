import unittest
from classes.budget_item import BudgetItem

class BudgetTest(unittest.TestCase):
    
    def test_budget_item_creation(self):
        test_item = BudgetItem(**{"Category": "Food", "Budget": 500, "Expense": 300})
        output = test_item.__str__()
        self.assertEqual(output, f"{test_item.category}\t  {test_item.budget}\t  {test_item.expense}")





if __name__ == '__main__':
    unittest.main()
    