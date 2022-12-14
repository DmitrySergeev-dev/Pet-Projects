from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug':self.slug})

# Create your models here.
