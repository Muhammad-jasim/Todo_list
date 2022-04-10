from django.db import models

# Create your models here.
class TodoList(models.Model):
    item_id = models.AutoField(primary_key=True)
    item = models.CharField(max_length=20)
    order = models.IntegerField(null=True,blank=True,unique=True)

    def __str__(self):
        return self.item