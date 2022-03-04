from  dbconnection import get_connection
import smtplib
from datetime import date

sender = 'ramyamarella554@gmail.com'
joiningdates=get_connection()
for joiningdate in joiningdates:
    print(joiningdate)
    import pdb;

    pdb.set_trace()
    if joiningdate[1] and joiningdate[1]==date.today():

        sender_email_id = 'ramyamarella554@gmail.com'

        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(sender_email_id, "ramya@554")
        message = "hello"
        s.sendmail(sender_email_id, joiningdate[2], message)
        s.quit()





# message ="Hello Welcome"
# try:
#    smtpObj = smtplib.SMTP('localhost')
#    smtpObj.sendmail(sender, receivers, message)
#    print "Successfully sent email"
# except SMTPException:
#    print "Error: unable to send email"
# server = smtplib.SMTP('smtp.gmail.com', 587)
# server.ehlo()
# server.starttls()
# fromaddress='ramyamarella554@gmail.com'
# password=input("enter the password")
#
#    # Next, log in to the server
# server.login(fromaddress,password)
#
#    # Send the mail
# msg = "Hello!"
# server.sendmail('ramyamarella554@gmail.com','ramyamarella554@gmail.com',msg)
# server.close()
# print('mail has sent')