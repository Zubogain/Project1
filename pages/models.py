from django.db import models

# Create your models here.
class posts(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content