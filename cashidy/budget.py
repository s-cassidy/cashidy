from fund import Fund

class Budget(Fund):
    # has: categories, category groups, accounts
    # can: make new categories

    def category_new(self):
        pass

    def category_del(self):
        pass


class Category(Fund):
    # has group
    pass

class ToBeBudgeted(Category):
    # special category containing unallocated money
    pass
