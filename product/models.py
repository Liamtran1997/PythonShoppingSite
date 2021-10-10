from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50, null=False)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'Category'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50, null=False)
    price = models.IntegerField(default=0, null=False)
    unit = models.IntegerField(default=0, null=False)
    is_deleted = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Product'

    def __str__(self):
        return self.name
