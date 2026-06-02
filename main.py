# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.

import smtplib
import datetime as dt
import random
import pandas
import os

PLACEHOLDER = "[NAME]"
MY_EMAIL = os.environ.get("MY_EMAIL")
PASSWORD = os.environ.get("MY_PASSWORD")
TEMPLATES = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

data = pandas.read_csv("birthdays.csv")
data.to_dict()

now = dt.datetime.now()

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
for (index, row) in data.iterrows():
    if row.month == now.month and row.day == now.day:
        recipient_email = row.email
        recipient_name = row.get("name")

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        template_name = random.choice(TEMPLATES)
        with open(f"letter_templates/{template_name}") as file:
            template = file.read()
        letter = template.replace(PLACEHOLDER, recipient_name)

# 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=recipient_email,
                msg=f"Subject:Happy Birthday!\n\n{letter}"
            )
