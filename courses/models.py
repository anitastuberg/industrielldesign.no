from django.db import models
from django.template.defaultfilters import slugify

from authentication.models import Profile


class CourseReview(models.Model):
    text = models.TextField()
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.text[:50] + '...'


class Course(models.Model):
    YEAR_CHOICES = [
        ('1.klasse', '1.klasse'),
        ('2.klasse', '2.klasse'),
        ('3.klasse', '3.klasse'),
        ('4.klasse', '4.klasse'),
        ('5.klasse', '5.klasse'),
        ('Ikke trinnavhengig', 'Ikke trinnavhengig')
    ]
    name = models.CharField(max_length=300)
    course_code = models.CharField(max_length=20, unique=True)
    reviews = models.ManyToManyField(CourseReview, blank=True)
    class_year = models.CharField(max_length=20, choices=YEAR_CHOICES, default="Ikke trinnavhengig")
    display_without_reviews = models.BooleanField(default=False)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            # Only set the slug when the object is created.
            self.slug = slugify(self.course_code)  # Or whatever you want the slug to use
        super(Course, self).save(*args, **kwargs)


class CourseLink(models.Model):
    url_title = models.CharField(max_length=500)
    url_description = models.TextField()
    img_url = models.CharField(max_length=500)
    url = models.CharField(max_length=500)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)
