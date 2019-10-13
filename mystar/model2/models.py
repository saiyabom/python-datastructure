from django.db import models
from model1.models import Model1
# Create your models here.
class Model2(models.Model):
    obj_name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)

    owner = models.ForeignKey(Model1, on_delete=models.CASCADE)