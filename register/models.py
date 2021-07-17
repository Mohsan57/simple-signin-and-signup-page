from django.db import models
from django.utils.text import slugify

# Create your models here.


class Register(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, null=False)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user_name)
        super(Register, self).save(*args, **kwargs)
