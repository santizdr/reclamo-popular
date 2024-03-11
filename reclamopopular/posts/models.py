from django.db import models
from django.core.validators import MinValueValidator 


# Create your models here.
class Post(models.Model):
    title = models.CharField(null=False, max_length=255)
    content = models.TextField(null=False)
    post_date = models.DateField(auto_now=False, auto_now_add=True)
    likes = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    def __str__(self):
        return str(self.title)