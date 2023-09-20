from datetime import datetime

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse

from .models import Event
from django.utils import timezone

# Create your tests here.
class EventsTest(TestCase):

    @staticmethod
    def get_date(delta):
        return timezone.now() + timezone.timedelta(days=delta)

    def get_absolute_url(self, slug):
        return "/event/%s" % slug

    def create_event(self):
        return Event.objects.create(title="Test event",
                                    description="Blah blah blah",
                                    location="IPD",
                                    image=SimpleUploadedFile(name='test_image.jpg', content=open('static_in_pro/our_static/img/about.jpg', 'rb').read(), content_type='image/jpeg'),
                                    event_start_time=timezone.now(),
                                    event_end_time=self.get_date(1),
                                    registration_required=True,
                                    registration_start_time=self.get_date(-1),
                                    alumni=False,
                                    class_1=False,
                                    class_2=False,
                                    class_3=True,
                                    class_4=True,
                                    class_5=True
                                    )

    def test_event_creation(self):
        event = self.create_event()
        self.assertTrue(isinstance(event, Event))
        self.assertEqual(event.slug, 'test-event')
        if not event.registration_start_time:
            self.assertEqual(event.registration_start_time, event.event_start_time)

    def test_event_detail_view(self):
        event = self.create_event()
        url = reverse('event', args=[event.slug])
        resp = self.client.get(url)
        self.assertEqual(url, self.get_absolute_url(event.slug))
        self.assertEqual(200, resp.status_code)
        self.assertIn(bytes(event.title, 'utf-8'), resp.content)


    def test_register_as_second_year_for_third_year_plus_event(self):
        event = self.create_event()
        user = self.create_user()
