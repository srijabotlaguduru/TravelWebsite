from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def send_signup_email(user_email):
    subject = 'Welcome to YourWebsite'
    html_message = render_to_string('email/signup_email.html')
    plain_message = strip_tags(html_message)
    from_email = 'vmanasa2003@gmail.com'
    to_email = user_email
    send_mail(subject, plain_message, from_email, [to_email], html_message=html_message)