import smtplib
import os
mailFrom = '***'

mailTo = '***'

mailSubject = 'Testowy mail '
mailBody = ''' 

'''

message = '''From: {}
Subject: {}
testowy mail wyslany przez skrypt w pythonie {}
'''.format(mailFrom, mailSubject, mailBody)

user = '***'

password = "***"

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    server.login(user,password)
    server.sendmail(user,mailTo,message)
    server.close()
    print('mail sent')
except:
    print('pojawił sie błąd')

