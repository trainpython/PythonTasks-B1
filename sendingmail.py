# import smtplib, ssl
#
# port = 587  # For starttls
# smtp_server = "smtp.gmail.com"
# sender_email = "ramyamarella554@gmail.com"
# receiver_email = "ramyamarella16@gmail.com"
# password = input("Type your password and press enter:")
# message = """\
# Subject: Hi there
#
# This message is sent from Python."""
#
# context = ssl.create_default_context()
# with smtplib.SMTP(smtp_server, port) as server:
#     server.ehlo()  # Can be omitted
#     server.starttls(context=context)
#     server.ehlo()  # Can be omitted
#     server.login(sender_email, password)
#     server.sendmail(sender_email, receiver_email, message)

# import smtplib
#
# sender = 'ramyamarella554@gmail.com'
# receivers = ['ramyamarella16@gmail.com']
#
# message = """From: From Person <from@fromdomain.com>
# To: To Person <to@todomain.com>
# Subject: SMTP e-mail test
#
# This is a test e-mail message.
# """
#
# try:
#    smtpObj = smtplib.SMTP('localhost')
#    smtpObj.sendmail(sender, receivers, message)
#    print("Successfully sent email")
# except smtplib.SMTPException:
#    print("Error: unable to send email")

import smtplib

# list of email_id to send the mail
li = ["xxxxx@gmail.com", "yyyyy@gmail.com"]
sender_email_id='ramyamarella554@gmail.com'

# for dest in li:
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(sender_email_id, "ramya@554")
message = "Message_you_need_to_send"
s.sendmail(sender_email_id, sender_email_id, message)
s.quit()