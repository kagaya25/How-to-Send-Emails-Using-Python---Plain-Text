# author: https://github.com/kagaya25/How-to-Send-Emails-Using-Python---Plain-Text

import smtplib
import ssl
import sys

smptp_server = 'smtp.gmail.com'
port = 587      # for that server
print("Mailing Starting ")
sender = input("Enter your email: ")
password = input("Enter your password: ")
context = ssl.create_default_context()    # creates secure SSl context
#   subject have to be in the first line after '/' sign
message = '''\
subscribe to my channel and like . 
'''
receiver = input("Enter your Send to : ")


try:
    server = smtplib.SMTP(smptp_server, port)
    server.ehlo()   # enable connecting to server
    server.starttls(context=context)  # secures the connection
    server.login(sender, password)
    server.sendmail(sender, receiver, message)
    print('Your mail is sent successfully.')
except Exception as e:
    sys.stderr.write("A problem occured: ")
    sys.stderr.flush()
    print(e)

finally:
    server.quit()
    print("Mailing Send  ")



'''
Note:
You have to allow less secure apps on chrome, otherwise Google will block your attempt to send an e-mail: myaccouns.google.com/lesssecureapps
'''