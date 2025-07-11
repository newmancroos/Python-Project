#import datetime as dt
import random
from datetime import datetime
import pandas
##################### Normal Starting Project ######################

import  smtplib
from email.message import EmailMessage

def send_email(email, quote):
    sender_email = "newmancroos@gmail.com"  # Replace with your email
    # sender_password = "lmsd nuko kbdo hjwk"  # Replace with your app password (for Gmail, generate one)
    sender_password = "lmsdnukokbdohjwk"  # Replace with your app password (for Gmail, generate one)
    receiver_email = email
    subject = "Birthday Wishes"
    body = quote

    # Create the email message
    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    # Connect to the SMTP server and send the email
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:  # Use SMTP_SSL for secure connection
            smtp.login(sender_email, sender_password)
            smtp.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

today = (datetime.now().month, datetime.now().day)

data = pandas.read_csv("birthdays.csv")
birthday_dic = {(data_row.month, data_row.day):data_row for (index, data_row) in data.iterrows()}

if today in  birthday_dic:
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    birthday_person=birthday_dic[today]
    person_email = birthday_person["email"]
    person_name = birthday_person["name"]

    with open(file_path, "r") as file:
        message = file.read()
        messge_to_send=message.replace("[NAME]", person_name)

    send_email(person_email,messge_to_send)


#HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT 1: Think about the relative file path to open each letter.
# HINT 2: Use the random module to get a number between 1-3 to pick a randome letter.
# HINT 3: Use the replace() method to replace [NAME] with the actual name. https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT 1: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
# HINT 2: Remember to call .starttls()
# HINT 3: Remember to login to your email service with email/password. Make sure your security setting is set to allow less secure apps.
# HINT 4: The message should have the Subject: Happy Birthday then after \n\n The Message Body.



