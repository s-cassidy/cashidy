from money import Pence

class MonthlyBudget:
    # has: to be budgeted
    # has: assignments, acivity
    # needs: categories
    def budget_for_category(self, amount: Pence, category: str) -> None:
        pass

    def reallocate_funds(self, amount: Pence, category_from: str, category_to: str):
        pass

    def category_activity(self, category: str):
        pass
    
