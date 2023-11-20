import smtplib
import datetime as dt
import random

MY_EMAIL = ""   # Enter your email
MY_PASSWORD = ""    # Enter your password

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0:    # weekday starts from monday as 0
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()     # read all the quotes in the file
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Subject:Monday Motivation\n\n{quote}")

