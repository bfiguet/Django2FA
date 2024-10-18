import os
#from twilio.rest import Client

import smtplib
from email.message import EmailMessage

def send_email(user_code, email):
	msg = EmailMessage()
	msg.set_content(f"Hi! This is your verification code for user {user_code}")
	msg['subject'] = '2FA code for PongGame'
	msg['to'] = email
	
	user = "email@gmail.com" #
	msg['from'] = user
	password = "sdfmdlfkdslkfnsd" #app password in gmail
	
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	server.login(user, password)
	server.send_message(msg)
	server.quit()

#You Account sid and Auth Token from twilio.com/console
#and set them as environment variables. See http://twil.io/secure
#account_sid = os.environ['TWILIO_ACCOUNT_SID']
#auth_token = os.environ['TWILIO_AUTH_TOKEN']
#client = Client(account_sid, auth_token)

#def send_sms(user_code, phone_number):
#	message = client.messages.create(
#		body=f"Hi! Your user and verification code is {user_code}",
#		from_='+33620216376',
#		to=phone_number
#	)
#	print(message.sid)
