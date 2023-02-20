from cashidy.budget.money import Pence


class MonthlyBudget:
    # has: to be budgeted
    # has: assignments, acivity
    # needs: categories
    def budget_for_category(self, amount: Pence, category: str) -> None:
        pass

    def reallocate_funds(self, amount: Pence, cat_from: str, cat_to: str) -> None:
        pass

    def category_activity(self, category: str) -> None:
        pass
