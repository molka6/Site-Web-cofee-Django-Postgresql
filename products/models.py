from django.db import models
from datetime import datetime
class Product(models.Model):
    name = models.CharField(max_length=150)
    description=models.TextField()
    price=models.DecimalField(max_digits=6,decimal_places=2)
    image=models.ImageField(upload_to='media/photos/%Y/%m/%d/')
    is_active=models.BooleanField(default=True)
    publish_date=models.DateTimeField(default= datetime.now)

    def ___str___(self):
        return self.description
    # ordre of data 
    class Meta: 
        ordering =['-publish_date'] 

        