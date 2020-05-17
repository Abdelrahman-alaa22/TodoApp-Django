from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.


class Task(models.Model):

    title = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})
