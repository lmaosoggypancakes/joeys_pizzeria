from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    pass
class Order(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    item = models.ManyToManyField("Item", related_name="order_items", symmetrical=False)

class Item(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()
    price = models.FloatField()
    img = models.URLField(null=True)
    def serialize(self):
        return {
            "title": self.title,
            "desc": self.desc,
            "price": self.price
        }
    def __str__(self):
        return self.title
class Application(models.Model):
    work_experince = models.CharField(max_length=10)
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    newsletter = models.BooleanField()
    questions = models.TextField()