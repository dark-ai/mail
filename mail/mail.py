import os
from datetime import datetime
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


class Writer(object):

    def __init__(self, my_address, password):
        self.my_address = my_address
        self.password = password
    
    def write(self, address, subject, content):
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = self.my_address
        msg['To'] = address
        msg['Date'] = str(datetime.now())
        msg.attach(MIMEText(content, 'html', 'utf-8'))
        return msg
    
    def send(self, msg):
        name, suffix = msg['From'].split('@')
        if suffix == '163.com':
            host = 'smtp.163.com'
        elif suffix == 'qq.com':
            host = 'smtp.qq.com'
        else:
            print(f'{suffix} is not supported')
            return False
        try:
            server = smtplib.SMTP()
            server.connect(host)
            server.login(msg['From'], self.password)
            server.sendmail(self.my_address, [msg['To']], msg.as_string())
            server.quit()
            return True
        except Exception as e:
            print(e)
            return False

