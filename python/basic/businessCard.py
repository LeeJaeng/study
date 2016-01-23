class BusinessCard:
    def __init__(self, name, email, addr):
        self.name = name
        self.email = email
        self.addr = addr

    def print_info(self):
        print('---------------------')
        print('Name: ', self.name)
        print('E-mail: ', self.email)
        print('Address: ', self.addr)
        print('---------------------')


def main():
    card1 = BusinessCard('Jaeng', 'good', '11')
    card1.print_info()


if __name__ == '__main__':
    main()
