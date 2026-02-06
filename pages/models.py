from django.db import models
from django.contrib.auth.models import User

class Page(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=150)
    content = models.TextField()
    image = models.ImageField(upload_to='pages/', blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
