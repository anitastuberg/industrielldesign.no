from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string


def email_sender(subject, template_name, receivers, context, sender=settings.EMAIL_HOST_USER):
    msg_html = render_to_string(template_name, context)
    msg = EmailMessage(subject=subject, body=msg_html, from_email=sender, bcc=receivers)
    msg.content_subtype = "html"  # Main content is now text/html
    return msg.send()


def send_signup_receipt(event):
    subject = "Du er nå påmeldt %s" % event.title
    context = {
        'event': event
    }
    emails = list(event.registered_users.values_list('email', flat=True))
    email_sender(subject, 'emails/signup-receipt.html', emails, context)
