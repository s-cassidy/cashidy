from fund import Fund

class Account(Fund):
    # has: name
    # can: reconcile
    pass

class RemoteAccount(Account):
    # for accounts that get their data from
    # an authoritative remote source, i.e.
    # import statements directly
    pass

class UserAccount(Account):
    # for account that must be manually
    # updated by the user (e.g. cash)
    pass
