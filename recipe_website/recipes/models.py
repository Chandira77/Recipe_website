from django.db import models

# Create your models here.
# class Recipe(models.Model):
#     name = models.CharField(max_length=100)
#     category = models.CharField(max_length=100)
#     description = models.TextField()
#     process = models.TextField()
#     ingredients = models.TextField()
#     picture = models.ImageField(upload_to='recipes/')

#     def __str__(self):
#         return self.name
    
    
class Recipes(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField()
    process = models.TextField()
    ingredients = models.TextField()
    picture = models.ImageField(upload_to='recipes/', null=True, blank=True)

    def __str__(self):
        return self.name