from django.db import models
# Create your models here.
class User(AbstractUser):
    pass

class Order(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="user")
    item = models.ManyToManyField("Item", related_name="order_items", symmetrical=False)

class Item(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()
    price = models.FloatField()
