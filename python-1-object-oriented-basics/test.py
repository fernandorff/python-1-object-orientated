def open_account(account_number, account_owner, account_balance, account_withdraw_limit):
    account = {"Account Number": account_number,
               "Account Owner": account_owner,
               "Account Balance": account_balance,
               "Withdraw Limit": account_withdraw_limit}
    return account


def deposit_balance(account, value):
    account["Account Balance"] += value


def withdraw_balance(account, value):
    account["Account Balance"] -= value


def check_balance(account):
    print("Account Balance: {}".format(account["Account Balance"]))


account1 = open_account(123, "Fernando", 666, 333)

print(account1)
check_balance(account1)
withdraw_balance(account1, 333)
check_balance(account1)
deposit_balance(account1, 222)
check_balance(account1)
