from monitoring.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

def check_alarm(value):
    if value >= 100:
        send_email_growing()
    elif value <= 60:
        send_email_decreasing()    
    return()

def send_email_growing():
    subject = 'Test heart rate'
    message = 'Warning!!! the heart rate is growing'
    recepient = "danielfelipe111@gmail.com"
    send_mail(subject, message, EMAIL_HOST_USER, [recepient])

def send_email_decreasing():
    subject = 'Test heart rate'
    message = 'Warning!!! the heart rate is decreasing'
    recepient = "danielfelipe111@gmail.com"
    send_mail(subject, message, EMAIL_HOST_USER, [recepient])