from django.core.mail import send_mail
from django.conf import settings
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class SendEmail:

    def __init__(self,subject:str,body:str,mail_sender:str,mail_receiver:str) -> None:
        self.subject=subject
        self.body=f"Mail From {mail_sender} : \n"+body
        self.mail_sender=settings.EMAIL_HOST_USER
        self.password=settings.EMAIL_HOST_PASSWORD
        self.mail_receiver=mail_receiver
        self.smtp_server=settings.EMAIL_HOST
        self.smtp_port=settings.EMAIL_PORT
    
    def send(self):
        try:
            message = MIMEMultipart()
            message['From'] = self.mail_sender
            message['To'] = self.mail_receiver
            message['Subject'] = self.subject
            message.attach(MIMEText(self.body, 'plain'))

            server=smtplib.SMTP_SSL(self.smtp_server, self.smtp_port)
            server.login(self.mail_sender, self.password)
            server.sendmail(self.mail_sender, self.mail_receiver, message.as_string())
        except Exception as e:
            raise Exception(str(e))