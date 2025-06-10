from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    title = models.CharField(max_length=200)
    keywords = models.TextField(help_text="کلمات کلیدی را با کاما جدا کنید")
    
    def get_keywords_list(self):
        return [k.strip().lower() for k in self.keywords.split(',')]

class UserResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField()
    progress = models.FloatField(default=0)  # درصد تطابق
    created_at = models.DateTimeField(auto_now_add=True)