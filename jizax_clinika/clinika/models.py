from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name


# class Video(models.Model):
#     video_url = models.URLField()
#
#     def __str__(self):
#         return self.video_url


class Blog(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='images/', blank=True, null=True)
    video_url = models.FileField(upload_to='videos/')
    body = models.TextField()

    def __str__(self):
        return self.name









