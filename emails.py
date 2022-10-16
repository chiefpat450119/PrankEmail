import smtplib
from email.message import EmailMessage
from time import sleep
from random import randint

recipients = input("Enter recipients separated by comma + space: ")
num_emails = int(input("Enter the number of emails to send: "))


def email(repeats):
	for i in range(repeats):
		msg = EmailMessage()
		mail_list = recipients.split(", ")
		num = randint(1, 10)
		msg["Subject"] = "Congratulations" + num*"!"
		msg["From"] = "noreply.xvideos1@gmail.com"
		msg["To"] = mail_list

		# Email body
		msg.set_content(
			f"Based on your recent searches on Xvideos, you have been selected as one of our lucky winners to benefit from a free 30-day subscription."
			f"This includes unlimited watch time and ad-free content."
			f"Click here to redeem your offer!"
			f"https://bit.ly/3AaKklR")

		with open("email.html") as email_format:
			msg.add_alternative(email_format.read(), subtype="html")


		with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
			smtp.login("noreply.xvideos1@gmail.com", "wygcugpbnkpczgpv")
			smtp.send_message(msg)


email(num_emails)
