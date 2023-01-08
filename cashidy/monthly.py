from money import Pounds

class MonthlyBudget:
    # has: to be budgeted
    # has: assignments, acivity
    # needs: categories
    def budget_for_category(self, amount: Pounds, category: str):
        pass

    def reallocate_funds(self, amount: Pounds, category_from: str, category_to: str):
        pass

    def category_activity(self, category: str):
        pass
    
