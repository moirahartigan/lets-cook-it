from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Categories(models.Model):
    name = models.CharField(max_length=220, unique=True)
    slug = models.SlugField(max_length=220, unique=True, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


#Recipes model
class Recipe(models.Model):
    title = models.CharField(max_length=220, unique=True)
    slug = models.SlugField(max_length=220, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='recipe')
    image_url = CloudinaryField('image_url', default='placeholder')
    recipe_url = models.URLField(null=True)
    ingredients = models.TextField()
    method = models.TextField()
    prep_time = models.CharField(max_length=5,)
    cook_time = models.CharField(max_length=5,)
    servings = models.CharField(max_length=2,)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)
    approved = models.BooleanField(default=False)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)

    # Using slugify found here https://kodnito.com/posts/slugify-urls-django/
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Recipe, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


# comments model
class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='comments')

    name = models.CharField(max_length=40)
    email = models.EmailField()
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.message} by {self.name}"
