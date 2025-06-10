from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    title = models.CharField(max_length=200)
    keywords = models.TextField(help_text="کلمات کلیدی را با کاما جدا کنید")
    
    def get_keywords_list(self):
        return [k.strip().lower() for k in self.keywords.split('_')]
