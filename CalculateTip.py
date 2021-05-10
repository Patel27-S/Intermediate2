#Prompts the user to enter the bill.
What_is_bill = float(input("Please let me know what your bill is : "))

#Prompts the user to enter the percentage he/she would like to tip.
Percentage_tip = float(input("Please let me know what percentage would you like to tip : "))

#Prints the total the user has to pay by adding the tip to total bill.
print("Okay, so that makes your total as {} :)".format(What_is_bill + (What_is_bill*Percentage_tip*0.01)))
