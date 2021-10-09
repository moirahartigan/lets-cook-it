from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Categories(models.Model):
    title = models.CharField(max_length=220, unique=True)

    def __str__(self):
        return self.title


class Recipe(models.Model):
    title = models.CharField(max_length=220, unique=True)
    slug = models.SlugField(max_length=220, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='recipes')
    image = CloudinaryField('image', default='placeholder')
    ingredients = models.TextField()
    method = models.TextField()
    prep_time = models.CharField(max_length=5,)
    cook_time = models.CharField(max_length=5,)
    servings = models.CharField(max_length=2,)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
