from django.db import models
from django.contrib.auth import get_user_model

class Receipt(models.Model):
  store_name = models.CharField(max_length=100)
  date_of_purchase = models.DateTimeField()
  item_list = models.TextField()
  user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
  total_amount = models.FloatField()
  
  def __str__(self) -> str:
    return f'[#{self.pk}]{self.user}-{self.store_name}'
