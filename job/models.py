from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFit, ResizeToFill
from django.core.validators import RegexValidator
from django.template.defaultfilters import slugify


class JobFilter(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=100)
    logo = ProcessedImageField(upload_to='komite/', processors=[ResizeToFit(
        500, 500, False)], format='png', options={'quality': 85}, null=True)
    color = models.CharField(max_length=7, validators=[RegexValidator(
        regex='^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$', message='Must be a hex code', code='nomatch')])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Bedrift"
        verbose_name_plural = "Bedrifter"


class BulletPoints():
    title = models.CharField(max_length=100)
    point = models.ExpressionList



class Job(models.Model):
    title = models.CharField(max_length=100)
    intro = models.TextField(max_length=200, null=True)
    deadline = models.DateTimeField()
    description = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    filters = models.ManyToManyField(JobFilter)
    external_link_1 = models.CharField(max_length=150, null=True, blank=True)
    link_text_1 = models.CharField(max_length=150, null=True, blank=True)
    external_link_2 = models.CharField(max_length=150, null=True, blank=True)
    link_text_2 = models.CharField(max_length=150, null=True, blank=True)
    external_link_3 = models.CharField(max_length=150, null=True, blank=True)
    link_text_3 = models.CharField(max_length=150, null=True, blank=True)
    slug = models.SlugField(blank=True, null=True)
    image = ProcessedImageField(upload_to='job/', processors=[ResizeToFit(1000, 1000, False)], format='JPEG',
                                options={'quality': 85}, null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Or whatever you want the slug to use
        self.slug = slugify(self.title + '-' + str(self.pk))
        super(Job, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Stillingsannonse'
        verbose_name_plural = 'Stillingsannonser'
