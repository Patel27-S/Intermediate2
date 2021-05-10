Enter_email = input("Please Enter your email address : ")

if ("gmail" or "yahoo" or "hotmail") in Enter_email:
    print("Wow, you have the email account with gmail/yahoo/hotmail domain :)")
else:
    print("Fantastic, seems like you have an email account with a custom domain :)")



#This generates the user name.
user_name = Enter_email.split('@')[0]
print(user_name, "is the user name.")

#This generates the domain name.
domain_name = Enter_email.split('@')[1].split('.')[0]
print(domain_name, "is the domain name.")