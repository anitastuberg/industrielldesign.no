from django.db import models
from django.template.defaultfilters import slugify


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Tip(models.Model):
    title = models.CharField(max_length=300, unique=True)
    html = models.TextField()
    tags = models.ManyToManyField(Tag)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            # Only set the slug when the object is created.
            self.slug = slugify(self.title)  # Or whatever you want the slug to use
        super(Tip, self).save(*args, **kwargs)


