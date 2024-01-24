from src.mail.serializers.email_serializer import EmailSerializerForInput
from src.mail.models import Email
import uuid
from django.conf import settings
from utils.emails.main import SendEmail
from django.utils import timezone
from celery import shared_task
from benedict import benedict
from threading import Thread

class EmailService:

    @staticmethod
    def send_mail(data:EmailSerializerForInput):
            mail=SendEmail(
                subject=data.subject,
                body=data.body,
                mail_sender=data.sent_mail,
                mail_receiver='utsavchatterjee71@gmail.com'
            )
            return mail.send()
    
    @staticmethod
    def save_mail_record(data:EmailSerializerForInput):
            email=Email(
                id=uuid.uuid1(),
                sent_email=data.sent_mail,
                host_email=settings.EMAIL_HOST_USER,
                subject=data.subject,
                body=data.body,
                sent_at=timezone.now()
            )
            return email.save()

    @staticmethod
    @shared_task
    def celery_task(validated_data:EmailSerializerForInput):
        validated_data=benedict(validated_data)
        try:
            EmailService.send_mail(validated_data)
            EmailService.save_mail_record(validated_data)
            return "Done"
        except Exception as e:

            mail_sender=validated_data.sent_mail
            subject="Failed!"
            body="Mail Sending is failed due some errors!"
            mail_receiver=validated_data.sent_mail

            mail=SendEmail(
            subject=subject,
            body=body,
            mail_sender=mail_sender,
            mail_receiver=mail_receiver
            )
            mail.send()
            return "Mail Failed"
    
    @staticmethod
    def thread_task(validated_data:EmailSerializerForInput):
        validated_data=benedict(validated_data)
        try:
            EmailService.send_mail(validated_data)
            EmailService.save_mail_record(validated_data)
            return "Done"
        except Exception as e:
        
            mail_sender=validated_data.sent_mail
            subject="Failed!"
            body="Mail Sending is failed due some errors!"
            mail_receiver=validated_data.sent_mail

            mail=SendEmail(
            subject=subject,
            body=body,
            mail_sender=mail_sender,
            mail_receiver=mail_receiver
            )
            mail.send()
            return "Mail Failed"

    
    @staticmethod
    def serve(data:dict):
            """
            data={
                "sent_mail":...,
                "subject":...,
                "body":...
            }
            """
            serializer=EmailSerializerForInput(data=data)
            if serializer.is_valid():
                validated_data=serializer.validated_data
                #EmailService.celery_task.delay(validated_data)
                t=Thread(target=EmailService.thread_task,args=[validated_data])
                t.start()
                return
            else:
                raise Exception(serializer.errors)