from django.db import models

class product(models.Model):
    p_id=models.AutoField
    p_name=models.CharField(max_length=50)