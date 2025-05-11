from datetime import datetime  
import pandas  
import random  
import smtplib  

# Your email credentials (Make sure to update these with your own credentials)
MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "YOUR PASSWORD"


today = datetime.now()  
today_tuple = (today.month, today.day)  # Store the current month and day in a tuple

data = pandas.read_csv("birthdays.csv")  
# Creating a dictionary where the keys are tuples of (month, day), and the values are the corresponding row data
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

# Check if today's date matches any birthday in the dictionary
if today_tuple in birthdays_dict:  
    birthday_person = birthdays_dict[today_tuple]  # Get the person's information from the dictionary
    
    # Randomly select a birthday letter template from the 'letter_templates' folder
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"  
    with open(file_path) as letter_file:  
        contents = letter_file.read()  
        contents = contents.replace("[NAME]", birthday_person["name"])  

    # Sending the birthday email using SMTP (email server)
    with smtplib.SMTP("smtp.gmail.com") as connection:  
        connection.starttls()  # Secure the connection using TLS encryption
        connection.login(MY_EMAIL, MY_PASSWORD)  
        connection.sendmail(
            from_addr=MY_EMAIL,  
            to_addrs=birthday_person["email"],  
            msg=f"Subject:Happy Birthday!\n\n{contents}"  
        )
