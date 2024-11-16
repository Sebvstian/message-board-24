from django.db import models

# Create your models here.

class Publication(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField() #or content 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title