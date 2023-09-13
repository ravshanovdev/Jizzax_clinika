from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Blog(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='images/', blank=True, null=True)
    body = models.TextField()

    def __str__(self):
        return self.name









