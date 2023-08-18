from django.db import models

class Item(models.Model):
   name  = models.CharField(max_length=100)
   brand = models.CharField(max_length=100)
   count = models.PositiveIntegerField()
   description = models.CharField(max_length=200)

def __repr__(self):
   return f'Item({self.name}, {self.brand}, {self.count})'