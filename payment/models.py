from django.db import models

# Create your models here.
class payment(models.Model):
    id=models.AutoField(primary_key=True)
 
    shenase_kharid=models.CharField(max_length=100)  
    mablagh=models.DecimalField(max_digits=10,decimal_places=2)
    tarikh=models.DateTimeField(auto_now_add=True)
    authority=models.CharField(max_length=200)  
    statu=models.CharField(max_length=20,default='موفق')
    def __str__(self):
        return f'payment for Order{self.order_id}'
