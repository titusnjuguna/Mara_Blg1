from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
#post models
class Post(models.Model):
    title= models.CharField(max_length=100)
    content=models.TextField()
    author= models.ForeignKey(User, on_delete= models.CASCADE)
    date_posted=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('Post-detail',kwargs={'pk':self.pk})
