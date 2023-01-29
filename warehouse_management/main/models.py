from django.db import models

class stock(models.Model):
    s_id=models.AutoField(primary_key=True, default=0)
    s_name=models.CharField(max_length=50)
    s_cost_per_unit=models.IntegerField()
    def __str__(self):
        return self.s_name
    
    
class sq(models.Model):
    s_name=models.ForeignKey(stock, on_delete=models.CASCADE)
    s_in=models.IntegerField(default=0)
    s_out=models.IntegerField(default=0)
    date=models.DateField()
    class Meta:
        unique_together = (("s_name", "date"))
        