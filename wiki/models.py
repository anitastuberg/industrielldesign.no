from django.db import models
from django.template.defaultfilters import slugify

CATEGORIES = (
    ('FYI', 'FYI'),
    ('LOL', 'LOL')
)

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=40, unique=True)
    slug = models.SlugField(max_length=60, blank=True)
    text = models.TextField()
    image = models.ImageField(blank=True, null=True)
    category = models.CharField(max_length=3, choices=CATEGORIES)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    #image = models.ImageField()

    def save(self, *args, **kwargs):
        if not self.id:
            #Only set the slug when the object is created.
            self.slug = slugify(self.title) #Or whatever you want the slug to use
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.title