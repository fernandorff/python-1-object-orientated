class Account:

    def __init__(self, account_id, owner, balance, withdraw_limit):
        self._Account__id = account_id
        self._Account__owner = owner
        self._Account__balance = balance
        self._Account__withdraw_limit = withdraw_limit
        print("--------------------------------")
        print("|        CREATE ACCOUNT        |")
        print("--------------------------------")
        print("- Constructing object at ... {}".format(self))
        print("- Account Id:", self._Account__id)
        print("- Account Owner:", self._Account__owner)
        print("- Account Balance:", self._Account__balance)
        print("- Account Withdraw Limit:", self._Account__withdraw_limit)

    def extract(self):
        print("--------------------------------")
        print("|        ACCOUNT EXTRACT       |")
        print("--------------------------------")
        print("- Account Id:", self._Account__id)
        print("- Account Owner:", self._Account__owner)
        print("- Account balance: {}".format(self._Account__balance))

    def deposit(self, value):
        print("--------------------------------")
        print("|        DEPOSIT FUNDS         |")
        print("--------------------------------")
        print("- Account Id:", self._Account__id)
        print("- Account Owner:", self._Account__owner)
        print("- Depositing $ {} ...".format(value))
        print("- Updated balance: $", self._Account__balance, "-> $", self._Account__balance + value)
        self._Account__balance += value

    def __withdraw_denied(self, value):
        if value > self._Account__balance or value > self._Account__withdraw_limit:
            print("--------------------------------")
            print("|     WITHDRAW FUNDS DENIED    |")
            print("--------------------------------")
            print("- Account Id:", self._Account__id)
            print("- Account Owner:", self._Account__owner)
            if value > self._Account__balance:
                print("- Insufficient funds !!!")
                print("- Your balance: $ {}".format(self._Account__balance))
                print("- Withdrawal value: $ {}".format(value))
            if value > self._Account__withdraw_limit:
                print("- Withdrawal limit exceeded !!!")
                print("- Withdraw limit: $ {}".format(self._Account__withdraw_limit))
                print("- Withdrawal value: $ {}".format(value))
            return

    def withdraw(self, value):
        self.__withdraw_denied(value)
        if not self.__withdraw_denied:
            print("--------------------------------")
            print("|        WITHDRAW FUNDS        |")
            print("--------------------------------")
            print("- Account Id:", self._Account__id)
            print("- Account Owner:", self._Account__owner)
            print("- Withdrawing $ {} ...".format(value))
            print("- Updated balance: $", self._Account__balance, "-> $", self._Account__balance - value)
            self._Account__balance -= value

    def transfer(self, value, to_account):
        print("--------------------------------")
        print("|        TRANSFER FUNDS        |")
        print("--------------------------------")
        print("- From account id: {}".format(self._Account__id))
        print("- To account id: {}".format(to_account._Account__id))
        print("- Transfering $ {} ...".format(value))
        self.withdraw(value)
        if value > self._Account__balance or value > self._Account__withdraw_limit:
            print("--------------------------------")
            print("|       TRANSFER DENIED        |")
            print("--------------------------------")
            return
        to_account.deposit(value)

    @property
    def withdraw_limit(self):
        return self._Account__withdraw_limit

    @withdraw_limit.setter
    def withdraw_limit(self, new_value):
        print("--------------------------------")
        print("|    CHANGE WITHDRAW LIMIT     |")
        print("--------------------------------")
        print("- Account Id:", self._Account__id)
        print("- Account Owner:", self._Account__owner)
        print("- Changing limit from $ {} to $ {}".format(self._Account__withdraw_limit, new_value))
        self._Account__withdraw_limit = new_value

    @staticmethod
    def bank_id():
        return "001"


account_1 = Account(1, "Fernando", 2500, 1000)
account_2 = Account(2, "Tatiana", 222, 1500)

account_1.extract()
account_1.deposit(50)
account_1.withdraw(25)
account_1.withdraw_limit = 1100
account_1.transfer(1200, account_2)
print(Account.bank_id())
