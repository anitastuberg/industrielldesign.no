from django.test import TestCase
from events.models import Event
from emails.email_sender import send_signup_receipt


# Create your tests here.

class EmailTests(TestCase):
    def confirmation_email_sent_to_multiple_users(self):
        event = Event.objects.all()[0]
        result = send_signup_receipt(event)

        # Checks if email was sent without any errors
        self.assertIs(result, True)
