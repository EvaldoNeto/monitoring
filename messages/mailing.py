import smtplib

"""This file contains functions and classes for sending emails
"""

"""Class to store data for the mail provider which will be responsible,
to send the email 
"""
class MailProvider():
    def __init__(self, smtp_server, login, password):
        self.smtp_server = smtp_server
        self.login = login
        self.password = password        

"""Class responsible to format the message to be sent. 
@TODO send attachment files and html type of email
"""
class Mail():
    def __init__(self, provider, to_addr_lst, cc_lst, subject, message):
        self.to_addr_lst = to_addr_lst
        self.subject = subject
        self.message = message
        self.provider = provider
        self.cc_lst = cc_lst

    def send(self):
        header = 'From: %s\n'%self.provider.login
        header += 'To: %s\n'%','.join(self.to_addr_lst)
        header += 'Cc: %s\n'%','.join(self.cc_lst)
        header += 'Subject: %s\n'%self.subject
        msg = header + "\n" + self.message

        server = smtplib.SMTP(self.provider.smtp_server + ":587")
        server.starttls()
        server.login(self.provider.login, self.provider.password)
        server.sendmail(self.provider.login, self.to_addr_lst, msg)
        server.quit()
