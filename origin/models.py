from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Question(models.Model):
    title = models.CharField(max_length=200)
    keywords = models.TextField(help_text="کلمات کلیدی را با کاما جدا کنید")
    
    def get_keywords_list(self):
        return [k.strip().lower() for k in self.keywords.split('_')]

class User_Answer(models.Model):
    Question = models.CharField(max_length=200)
    answer = models.TextField()
    Date = models.DateTimeField(auto_now=timezone.now,blank=True)
