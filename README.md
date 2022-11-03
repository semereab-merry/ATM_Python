# ATM_classes

## Description
United Bank is looking at computerizing its banking system. The users of the system will interact with it like customers using an ATM. A part of their software requirement is given below. You are required to do additional self-study on how ATM machines function and create a design for managing the same.

## Requirements  
*	A list of all classes (related attributes and behaviors), relationships between classes, and assumptions made.
*	UML class diagram with all class relationships included.
*	Python code that represents classes, which includes the constructor, setter/getter, and other functions for the given requirements.

## File Structures: 
The files used in this program are:
•	Main.py: a python file which stores all the classes, attributes, and functions 
•	Bank.txt: a text file that stores the ATM ID and ATM location of an ATM whose money amount is less than 10% of the maximum amount. 
•	Users.txt: a text file that stores all the relevant information about each user created or updated
•	Account.txt: a text file that stores all the relevant information about each account opened or created 


## User process 
The user approaches the ATM and inserts his card.. The ATM checks if the account is saving, checking or business and asks the user which transaction he wants to do. The ATM asks for pin number and the user enters the pin number. Before doing the transaction, the ATM validates the pin entered by the user and gives 3 tries for the user to try. After 3 trial the user is forced to exit the system. If the pin is correct the user is allowed to do the transaction and whatever transaction he does, it affects his account accordingly. After each transaction the ATM removes the card and exits the program. If the user is willing to do another transaction, he should insert his card again and do the same process all over again.
(I considered the user as ‘he’)

## Flow Chart


## Class Design 
* User – Bank (Aggregation): A user can exist without the need for existence of a bank, hence I used aggregation for this relationship to indicate Users are part of the bank.  For every bank there can be many users.
* User – Account (Composition): An account cannot exist without a user, hence I used composition for this relationship to indicate Accounts are part of the User in this system. For every user there can be many Accounts opened.
* Accounts – Bank (Inheritance): Business account is a type of Account, so I used inheritance to show this relationship.
* Bank – ATM (Strong Association): A Bank has an ATM, and ATM has a Bank name. I used strong relationship to indicate that the relationship is established through their objects. For every bank there can be many ATMs.
* Bank – Account (Association): A Bank can create many accounts based on the preferences of the user. For every Bank there are many accounts.
* ATM – Account (Association): An ATM takes an action on the accounts. It can withdraw, deposit or transfer money. I used association to show this relationship. Many ATMs can take an action on many Accounts.



## Conclusion 
I have learned how to implement real-life problems into python codes in this exercise. I enjoyed designing UML and writing the codes as I was eager to program the functionalities of an ATM machine. However, I did not remember about the flow chart much, so I was forced to revise introduction to python, and it took me a bit of time to do it. On the other hand, saving all the relative information and accessing it to validate was a bit challenging as we did not work to this much of codes, but at the same time it let me to learn more about how to update, manipulate and edit text files. I would love working this project in GUI, but since there was not enough time, I was limited to the requirements given. From my perspective, I would suggest if the system would limit a user from not exceeding a specific number of accounts, because the system I have built added as many as accounts the user wants to add as long as he/she provides their User ID. In addition, functionalities like language could be added to the system to make it more user friendly. 
