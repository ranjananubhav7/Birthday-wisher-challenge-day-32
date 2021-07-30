import datetime as dt
import csv
import random
import smtplib

sender_mail = "birthdaywisheranubhav@gmail.com"
sender_password = "qwertyuiop@12345"
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
to_mail = []
name = []
is_birthday = 0
c = 0
with open("birthdays.csv") as file:
    content = csv.reader(file)
    for data in content:
        if int(data[3]) == dt.datetime.now().month and int(data[4]) == dt.datetime.now().day:
            to_mail.append(data[1])
            name.append(data[0])
            is_birthday = 1
            c += 1

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
#     name from birthdays.csv
if is_birthday == 1:
    while c > 0:
        with open(f"letter_templates/letter_{random.randrange(1, 4)}.txt") as letter:
            content = letter.read()
            message = content.replace("[NAME]", name[c-1])

        # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            # to secure the connection
            connection.starttls()
            # login
            connection.login(user=sender_mail, password=sender_password)
            connection.sendmail(
                from_addr=sender_mail,
                to_addrs=to_mail[c-1],
                msg=f"subject:Happy Birthday {name[c-1]}\n\n{message}"
            )
        c -= 1



