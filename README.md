# ATM transaction
This code implements a basic ATM system using Python and MySQL. The system allows users to perform various banking operations such as registering a new account, withdrawing and depositing money, checking account balance, viewing customer details, and closing an account. Here's an overview of each function:

Functions Overview
1.RegisterAcc()
This function registers a new account by collecting user details such as name, account number, PIN, card number, and opening balance. It then stores this information in a MySQL database.

AmountWithdrawl()
This function allows users to withdraw a specified amount of money from their account. It verifies the account and card number, calculates the new balance, and updates it in the database.

DepositAmount()
This function allows users to deposit money into their account. It verifies the account and card number, calculates the new balance, and updates it in the database.

customerDetails()
This function retrieves and displays all details of a customer based on their account number.

balanceEnquiry()
This function allows users to check the balance of their account by entering their card number.

CloseAcc()
This function deletes a customer's account details from the database based on the card number, effectively closing the account.

account()
This function serves as the main menu for the ATM system. It presents the user with a list of options and calls the appropriate function based on the user's selection.

