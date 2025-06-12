from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Catagory(models.Model):
    title=models.CharField(max_length=200)
    slug=models.SlugField()
    status=models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    title = models.CharField(max_length=200)
    keywords = models.TextField(help_text="کلمات کلیدی را با کاما جدا کنید")
    catagory=models.ManyToManyField(Catagory,related_name='questions',blank=True,null=True)

    def __str__(self):
        return self.title
    
    def get_keywords_list(self):
        return [k.strip().lower() for k in self.keywords.split('_')]
    