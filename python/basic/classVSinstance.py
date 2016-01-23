class Account:
    num_accounts = 0

    def __init__(self, name):
        self.name = name
        Account.num_accounts += 1

    def __del__(self):
        Account.num_accounts -= 1


def main():
    a = Account("a")
    print(Account.num_accounts)
    b = Account("b")
    print(Account.num_accounts)


if __name__ == '__main__':
    main()
