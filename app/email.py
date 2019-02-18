from flask_mail import Message
from flask import render_template
from . import mail

#craeting logic for the emails
def mail_message(subject,template,to,**kwargs):
    sender_email ='manowfelow@gmail.com'

    email = Message(subject, sender=sender_email, recipients=[to])
    email.body= render_template(template + ".txt",**kwargs)
    email.html = render_template(template + ".html",**kwargs)