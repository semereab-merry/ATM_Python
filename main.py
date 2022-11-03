# importing time to identify the years an account has been activate
import datetime
# importing random to generate random integer values
import random


class Account:
    """information about each account that a user owns"""

    def __init__(self):
        # initializing attributes
        self.Account_type = ('Checking', 'Saving', 'Business')
        self.type = 0
        self.Pin_key = ""
        self.Interest = 0.0
        self.Amount_total = 0
        self.Max_withdraw = 0
        self.Min_balance = 0
        self.Opening_year = datetime.datetime.now()

    # setter and getter
    def Set_account_type(self, type1):
        self.type = int(type1)

    def Set_pin_key(self, pin):
        self.Pin_key = pin

    def Set_opening_year(self, date1):
        self.Opening_year = date1

    def Set_amount(self, amount):
        self.Amount_total = amount

    def Get_amount(self):
        return self.Amount_total

    def Get_account_type(self):
        return self.Account_type[self.type]

    def Get_pin_key(self):
        return self.Pin_key

    def Get_opening_year(self):
        return datetime.strftime(self.Opening_year.date(), '%d/%m/%Y')

    # deposit function adds the amount entered to the amount total
    def deposit(self, amount=0):
        self.Amount_total += amount

    # withdraw function that subtracts the amount given from the total amount
    def withdraw(self, amount=0):
        # checking for each type as they have different minimum and maximum values
        if self.type == 0:
            self.Max_withdraw = 5000
            self.Min_balance = 100
            if amount <= self.Max_withdraw and self.Amount_total - amount > self.Min_balance:
                self.Amount_total -= amount
            elif amount > self.Max_withdraw:
                print("No more than 5000 AED cash withdrawal allowed")
            else:
                print("Insufficient funds")

        elif self.type == 1:
            self.Max_withdraw = 2000
            self.Min_balance = 1000
            if amount <= self.Max_withdraw and self.Amount_total - amount > self.Min_balance:
                self.Amount_total -= amount
            elif amount > self.Max_withdraw:
                print("No more than 2000 AED cash withdrawal allowed")
            else:
                print("Insufficient funds")

        else:
            self.Max_withdraw = 10000
            self.Min_balance = 2000
            if amount <= self.Max_withdraw and self.Amount_total - amount > self.Min_balance:
                self.Amount_total -= amount
            elif amount > self.Max_withdraw:
                print("No more than 10000 AED cash withdrawal allowed")
            else:
                print("Insufficient funds")

    # get amount function that gets the total amount for an account adding the interest over years
    def Get_total_amount(self):
        thisyear = datetime.datetime.now().year
        birthyear = datetime.datetime.strptime(self.Opening_year(), "%d/%m/%Y").year
        amount_years = int(birthyear) - int(thisyear)
        if self.type == 0:
            self.Interest = 0.03
        elif self.type == 1:
            self.Interest = 0.07
        elif self.type == 2:
            self.Interest = 0.03

        self.Amount_total += self.Interest * self.Amount_total * amount_years

    # a function that submits all the information of an account to a text file
    def submit(self):
        handler = open('account.txt', 'a')
        handler.write("Pin:{} Amount:{} Account Type:{} Interest:{} Opening-date:{}\n".format(self.Get_pin_key(),
                                                                                              self.Get_total_amount(),
                                                                                              self.Get_account_type(),
                                                                                              self.Interest,
                                                                                              self.Get_opening_year()))


class Business(Account):
    """information about a business type of an account """

    def __init__(self):
        # initializing
        Account.__init__(self)
        self.Account_type = 'Business'
        self.Business_name = ""
        self.Business_regs = ""
        self.Business_owner = ""

    # setter and getter
    def Set_bus_name(self, name):
        self.Business_name = name

    def Set_bus_regs(self, regs):
        self.Business_regs = regs

    def Set_bus_owner(self, owner):
        self.Business_owner = owner

    def Get_bus_name(self):
        return self.Business_name

    def Get_bus_regs(self):
        return self.Business_regs

    def Get_bus_owner(self):
        return self.Business_owner

    # a function that submits all the information of an account to a text file
    def submit2(self):
        handler = open('account.txt', 'a')
        handler.write(
            "Pin:{} Amount:{} Account Type:{} Interest:{} Opening-date:{} Business-name:{} "
            "Business-registration:{} Business-owner:{} \n".format(
                self.Get_pin_key(),
                self.Get_amount(),
                self.Account_type,
                self.Interest,
                self.Get_opening_year(),
                self.Get_bus_name(), self.Get_bus_regs(), self.Get_bus_owner()))


class User:
    """Information about a user of that has lists of accounts """

    # initializing
    def __init__(self):
        self.__User_id = ""
        self.__User_name = ""
        self.__User_address = ""
        self.__Phone_num = ""
        self.__Second_user_name = ""
        self.accounts = []

    # setter and getter
    def Set_user_id(self, id1):
        self.__User_id = id1

    def Set_user_name(self, name):
        self.__User_name = name

    def Set_user_address(self, address):
        self.__User_address = address

    def Set_second_user_name(self, name):
        self.__Second_user_name = name

    def Set_phone_num(self, num):
        self.__Phone_num = num

    def Set_accounts(self, acc=Account()):
        self.accounts.append(str(acc.Get_account_type()))

    def Get_user_id(self):
        return self.__User_id

    def Get_user_address(self):
        return self.__User_address

    def Get_phone_num(self):
        return self.__Phone_num

    def Get_accounts(self):
        return ' '.join(self.accounts)

    def Get_user_name(self):
        return self.__User_name

    def Get_second_name(self):
        return self.__Second_user_name

    # a function that submits all the information of a user to a text file
    def submit(self):
        handler = open('users.txt', 'a')
        handler.write("ID:{} Name:{},{}  Address:{} Phone number:{}, {}\n".format(self.Get_user_id(),
                                                                                  self.Get_user_name(),
                                                                                  self.Get_second_name(),
                                                                                  self.Get_user_address(),
                                                                                  self.Get_phone_num(),
                                                                                  self.Get_accounts()))


class Bank:
    """information about a bank that has set of users and their accounts """

    # initializing
    def __init__(self):
        self.__Bank_name = ""
        self.__Bank_address = ""
        self.__Users = {}
        self.account = Account()

    # setter and getter
    def Set_bank_name(self, name):
        self.__Bank_name = name

    def Set_bank_adress(self, address):
        self.__Bank_address = address

    def Set_users(self, user=User()):
        self.__Users[user.Get_user_name()] = user.Get_accounts()

    def Get_bank_name(self):
        return self.__Bank_name

    def Get_bank_adress(self):
        return self.__Bank_address

    def Get_accounts(self):
        return self.__Users

    # a function that creates an account when the user enters the correct user id
    def Create_new_account(self, id2):
        # opening the text files used as storages, some for reading the lines and some for editing
        handle = open("users.txt", "r")
        handle2 = open("users.txt", "a")
        handle1 = open("account.txt", "a")
        lines = handle.readlines()
        for information in lines:
            sentence = information.split()
            # checks if the id entered is correct or not
            if "ID:" + str(id2) == str(sentence[0]):
                self.account.Set_account_type(input("Enter 0 to set account to checking 1 to saving 2 to business: "))
                self.account.Set_amount(0)
                self.account.Set_opening_year(datetime.datetime.now())

                # updates the sentence in which the id was given, and adds the new account opened by the user
                update = sentence[-1].split()
                update.append(str(self.account.Get_account_type()))
                sentence[-1] = ",".join(update)
                handle2.write(' '.join(sentence) + "\n")

                # setts interest rates for checking and saving accounts
                if self.account.type == 0:
                    self.account.Interest = 0.03

                elif self.account.type == 1:
                    self.account.Interest = 0.07

                # enters the relevant information if the new account is business account
                if self.account.type == 2:
                    self.account = Business()
                    self.account.Set_pin_key(input("Insert new pin: "))
                    self.account.Interest = 0.03
                    # seed random number generator
                    random.seed(0)
                    # Generated random between 10000 to 99999 i.e, 5 digits for registration number
                    self.account.Set_bus_regs(random.randint(10000, 99999))
                    self.account.Set_bus_name(input("Enter Business Name: "))
                    self.account.Set_bus_owner(input("Enter Business owner: "))
                    # adds the new account to the text
                    handle1.write(
                        "Pin:{} Amount:{} Account Type:{} Interest:{} Opening-date:{} Business-name:{} "
                        "Business-registration:{} Business-owner:{} \n".format(
                            self.account.Get_pin_key(),
                            self.account.Get_amount(),
                            self.account.Account_type,
                            self.account.Interest,
                            self.account.Get_opening_year(),
                            self.account.Get_bus_name(), self.account.Get_bus_regs(), self.account.Get_bus_owner()))

                    break           # exits the loop when the necessary document is done

                else:
                    self.account.Set_pin_key(input("Insert new pin: "))
                    # adds the new account to the text
                    handle1.write(
                        ("Pin:{} Amount:{} Account Type:{} Interest:{} Opening-date:{}\n".format(
                            self.account.Get_pin_key(),
                            self.account.Get_amount(),
                            self.account.Get_account_type(),
                            self.account.Interest,
                            self.account.Get_opening_year())))
                    break            # exits the loop when the necessary document is done

        else:  # prints incorrect if the input doesnt match with user id
            print("Incorrect User ID")


class ATM:
    """information about ATM of a bank"""

    # initializing
    def __init__(self):
        self.__Atm_id = ""
        self.Bank = ""
        self._Amount_money = 0
        self._Max_amount = 0
        self._Atm_address = ""
        self.Types_currency = ('AED', 'USD')
        self._type_currency = 0
        self.pin = ""
        self.account = Account()

    # setter and getter
    def Set_atm_id(self, id2):
        self.__Atm_id = id2

    def Set_amount_money(self, amount):
        self._Amount_money = amount

    def Set_max_amount(self, amount):
        self._Max_amount = amount

    def Set_atm_address(self, address):
        self._Atm_address = address

    def Set_types_currency(self, type2):
        self._type_currency = type2

    def Set_bank(self, bank=Bank()):
        self.Bank = bank.Get_bank_name()

    def Get_atm_id(self):
        return self.__Atm_id

    def Get_bank(self):
        return self.Bank

    def Get_amount_money(self):
        return self._Amount_money

    def Get_max_amount(self):
        return self._Max_amount

    def Get_atm_address(self):
        return self._Atm_address

    def Get_types_currency(self):
        return self.Types_currency[self._type_currency]

    # a function that quits the system when triggered
    def remove_card(self):
        raise SystemExit()

    # a function that authenticates for the pin entered by the user,
    # in third trial the function calls remove card and forces the user to exit
    def authenticate(self):
        taking_input = True

        count = 0
        while taking_input:
            try:
                count += 1
                if int(count) == 4:         # because count is counting before the input, it needs to be stopped in 4
                    taking_input = False
                    print("You have tried 3 times, please contact you Bank!")
                    self.remove_card()
                handle = open("account.txt", "r")
                lines = handle.readlines()
                pin = input("Enter a pin")
                self.pin = str(pin)
                for information in lines:
                    sentence = information.split()
                    if "Pin:" + str(self.pin) == str(sentence[0]):
                        print(" ".join(sentence))
                        return

                else:  # raise error if the input doesnt match with all the values in the file
                    raise ValueError

            except ValueError:
                print("Enter correct pin")

    # a function that withdraws money from the ATM total money
    # and calls the withdraw function of an account after it authenticates the pin
    def Withdraw(self, amount):
        self.authenticate()
        if self._Amount_money > self._Max_amount * 0.1:
            if self._type_currency == 0:
                self._Amount_money -= amount
                self.account.withdraw(amount)
            elif self._type_currency == 1:
                new_amount = amount * 3.6
                self._Amount_money -= new_amount
                self.account.withdraw(new_amount)
        else:
            handle = open("bank.txt", "a")
            handle.write(str(self.Get_atm_id()) + " in " + str(self.Get_atm_address() + "is about to be empitied"))

        self.remove_card()

    # a function that deposits money to the ATM total money
    # and calls the deposit function of an account after it authenticates the pin
    def Deposit(self, amount2):
        self.authenticate()
        if self._type_currency == 0:
            self._Amount_money += amount2
            self.account.deposit(amount2)
        elif self._type_currency == 1:
            new_amount = amount2 * 3.6
            self._Amount_money += new_amount
            self.account.deposit(new_amount)
        self.remove_card()

    # a function that transfers amount of money to other users
    # and calls the withdraw function of an account after it authenticates the pin
    def transfer(self, toAccount, amount):
        self.authenticate()
        # it withdraws money from the account and deposits money to the other account
        if self.account.withdraw(amount):
            toAccount.deposit(amount)
        else:
            print("Transfer unsuccessful")
