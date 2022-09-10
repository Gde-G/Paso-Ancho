from django.db import models

# Create your models here.

class Consulta(models.Model):
    name = models.CharField(max_length=120, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    question = models.TextField(max_length=2000, blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering =['-created']