import smtplib
from email.message import EmailMessage

# Email details
sender_email = "newmancroos@gmail.com"  # Replace with your email
sender_password = "lmsd nuko kbdo hjwk"  # Replace with your app password (for Gmail, generate one)
receiver_email = "newmancroos@yahoo.com"  # Replace with the recipient's email
subject = "Hello from Python!"
body = "This is a test email sent from a Python script."

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

    #-----------------------------------------------------------------------------------------------
import datetime as dt
import random
import  smtplib
from email.message import EmailMessage

def send_email(quote):
    sender_email = "newmancroos@gmail.com"  # Replace with your email
    # sender_password = "lmsd nuko kbdo hjwk"  # Replace with your app password (for Gmail, generate one)
    sender_password = "lmsdnukokbdohjwk"  # Replace with your app password (for Gmail, generate one)
    receiver_email = "newmancroos@yahoo.com"  # Replace with the recipient's email
    subject = "Quote of the day"
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
    # with smtplib.SMTP("smtp.gmail.com") as connection:
    #     connection.starttls()
    #     connection.login(user=sender_email,password=sender_password )
    #     connection.sendmail(
    #         from_addr=sender_email,
    #         to_addrs= receiver_email,
    #         msg= body
    #     )

now = dt.datetime.now()
year = now.year
month=now.month
day = now.day
day_of_week = now.weekday()

with open("quotes.txt") as file:
    all_quote= file.readlines()


quote_of_the_day = random.choice(all_quote)
print(quote_of_the_day)
if day_of_week==1:
    send_email(quote_of_the_day)


