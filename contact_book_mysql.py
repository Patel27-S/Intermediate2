import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = '*****',
    passwd = '*****',
    database = 'information_details'
    )

cursor = mydb.cursor()

#cursor.execute('SHOW DATABASES')

#cursor.execute('CREATE DATABASE INFORMATION_DETAILS')

#cursor.execute('CREATE TABLE contact_details( Sr_No int PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(50), Contact_Number bigint, Email_Address VARCHAR(100))')

#cursor.execute('ALTER TABLE contact_details MODIFY COLUMN Contact_Number BIGINT')

flag = True

while flag:

    name_prompt = input('Please enter the contact name or type "quit" if there are not any : ')
    if name_prompt == 'quit':
        print('Thank you! All the contact(s) have been saved.')
        flag = False
        exit()

    try:
        contact_number_prompt = int(input('Please enter the contact number of the person : '))
    except:
        print('Error : Please enter the digits for the contact number.')
        exit()
    
    email_address_prompt = input('Please enter the email address of the person : ')
    
    cursor.execute('INSERT INTO contact_details (Name, Contact_Number, Email_Address) VALUES(%s,%s,%s)',(name_prompt, contact_number_prompt, email_address_prompt))
    
    mydb.commit()


# Viewing the Database upon entering the data :-

cursor.execute('SELECT * FROM contact_details')

print(cursor.fetchone())
print(cursor.fetchmany(3))
print(cursor.fetchall())






