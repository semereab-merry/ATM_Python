# ATM_classes

## Description
United Bank is looking at computerizing its banking system. The users of the system will interact with it like customers using an ATM. A part of their software requirement is given below. You are required to do additional self-study on how ATM machines function and create a design for managing the same.

# Problem Analysis
## List of Classes, Attributes, And Behaviors

| Class names   |Attributes |  Behaviors |
|---------------|------------|------------|
| User |  User_id: (str)<br> User_name: (str) <br> User_address: (str) <br> Phone_num: (str) <br> Second_user_name: (str) <br> Accounts = [Account] | Set_user_id (str): <br> Set_user_name (str): <br> Set_user_adress (str): <br> Set_phone_num (str):<br>Set_account (Account ()):<br>Set_second_user_name (str):<br>Get_user_id (): str<br>Get_user_name ():str<br>Get_second_name ():str<br>Get_user_adress ():str<br>Get_phone_num ():str<br>Get_account (): list<br>Submit():|
| Account |  Account_type (‘Checking’, ‘Saving’, ‘Busines’)<br> Type: (int)<br>Pin_key: (Str)<br>Interest: (int)<br>Max_withdraw: (int)<br>Min_balance : (int)<br>Opening_year: (datetime)<br>Amount_total: (int) | Set_pin_key (str):<br>Set_amount(int):<br>Set_account_type (int):<br>Set_opening_year(datetime):<br>Get_pin_key ():str<br>Get_amount (): int<br>Get_account_type (): <br>Account_type[Type]<br>Get_opening_year (): datetime<br>withdraw ():<br>deposit ():<br>Submit ():|
| ATM |  Atm_id: (str)<br>Bank: (Bank ())<br>Amount_money: (int)<br>Max_amount: (int)<br>Atm_address: (str)<br>Types_currency (AED, USD)<br>type_currency: (int)<br>Pin: (str)<br>Account: (Account ())| Set_atm_id(str): <br>Set_amount_money(int): <br>Set_atm_address(str):<br> Set_types_currency(int): <br> Set_max_amount(int): <br>Set_bank(Bank()):<br>Get_atm_id (): str<br>Get_bank (): str<br>Get_amount_money (): int<br>Get_max_amount(): int<br>Get_atm_address (): str<br>Get_types_currency(): <br> Types_currency[types_currency]<br>Remove_card():<br>Authenticate (Pin):<br>Withdraw ():<br>Deposit ():<br>transfer ():|
| Bank |  Bank_name: (str)<br>Bank_address: (str)<br>Account: (Account ())<br>Users = {User_name (), Accounts}<br>+ATM: (ATM())| Set_bank_name (str):<br> Set_bank_adress (str):<br> Set_users (User):<br> Set_atm (ATM):<br> Get_atm(): str<br> Get_bank_name ():str<br> Get_bank_adress ():str<br> Get_users (): dict <br> Create_new_account (Account ()):|


## Understanding the problem
This program is created for an ATM of a given bank.  The bank has many users which has many accounts. A user can create an account in the bank and specify the account type and pin number for that account. For every account there is a specific pin number set by the user and different minimum and maximum amounts and doing any transaction is limited by those numbers. The ATM allows the user to deposit, withdraw and transfer money after validating his/her pin number. After a user creates an account, all the relevant information is stored in a file. And after a user is registered in the bank, all relevant information is stored in another file. Also, the bank has information about each user and his/her active accounts. 

## File Structures: 
The files used in this program are:
*	Main.py: a python file which stores all the classes, attributes, and functions 
*	Bank.txt: a text file that stores the ATM ID and ATM location of an ATM whose money amount is less than 10% of the maximum amount. 
*	Users.txt: a text file that stores all the relevant information about each user created or updated
*	Account.txt: a text file that stores all the relevant information about each account opened or created 


## User process 
The user approaches the ATM and inserts his card.. The ATM checks if the account is saving, checking or business and asks the user which transaction he wants to do. The ATM asks for pin number and the user enters the pin number. Before doing the transaction, the ATM validates the pin entered by the user and gives 3 tries for the user to try. After 3 trial the user is forced to exit the system. If the pin is correct the user is allowed to do the transaction and whatever transaction he does, it affects his account accordingly. After each transaction the ATM removes the card and exits the program. If the user is willing to do another transaction, he should insert his card again and do the same process all over again.
(I considered the user as ‘he’)

## Flow Chart
<img width="538" alt="image" src="https://user-images.githubusercontent.com/59441158/199777215-514e6830-3f76-46d5-b8cb-22e1d491309c.png" style="display: block; margin-left: auto; margin-right: auto;" >


## Class Design 
* User – Bank (Aggregation): A user can exist without the need for existence of a bank, hence I used aggregation for this relationship to indicate Users are part of the bank.  For every bank there can be many users.
* User – Account (Composition): An account cannot exist without a user, hence I used composition for this relationship to indicate Accounts are part of the User in this system. For every user there can be many Accounts opened.
* Accounts – Bank (Inheritance): Business account is a type of Account, so I used inheritance to show this relationship.
* Bank – ATM (Strong Association): A Bank has an ATM, and ATM has a Bank name. I used strong relationship to indicate that the relationship is established through their objects. For every bank there can be many ATMs.
* Bank – Account (Association): A Bank can create many accounts based on the preferences of the user. For every Bank there are many accounts.
* ATM – Account (Association): An ATM takes an action on the accounts. It can withdraw, deposit or transfer money. I used association to show this relationship. Many ATMs can take an action on many Accounts.

<img width="497" alt="image" src="https://user-images.githubusercontent.com/59441158/199777290-c7e17fe9-ed67-4ecf-b952-782ea119c2c6.png" style="display: block; margin-left: auto; margin-right: auto;" >

## Conclusion 
I have learned how to implement real-life problems into python codes in this exercise. I enjoyed designing UML and writing the codes as I was eager to program the functionalities of an ATM machine. However, I did not remember about the flow chart much, so I was forced to revise introduction to python, and it took me a bit of time to do it. On the other hand, saving all the relative information and accessing it to validate was a bit challenging as we did not work to this much of codes, but at the same time it let me to learn more about how to update, manipulate and edit text files. I would love working this project in GUI, but since there was not enough time, I was limited to the requirements given. From my perspective, I would suggest if the system would limit a user from not exceeding a specific number of accounts, because the system I have built added as many as accounts the user wants to add as long as he/she provides their User ID. In addition, functionalities like language could be added to the system to make it more user friendly. 
