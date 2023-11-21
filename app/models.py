from django.db import models
from django.utils.text import slugify
class Skills(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
class Author(models.Model):
    name = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    def __str__(self):
        return self.name
class Location(models.Model):
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    zip = models.CharField(max_length=200)
    def __str__(self):
        return self.street
class JobPost(models.Model):
    title = models.CharField(max_length=200, default='')
    description = models.CharField(max_length=200, default='')
    date = models.DateTimeField(auto_now_add=True)
    expiry = models.DateField(null=True)
    salary = models.IntegerField()
    slug = models.SlugField(null=True, unique = True)
    #relations one-to-one
    location = models.OneToOneField(Location,on_delete = models.CASCADE, null = True)
    #relations many-to-one
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    #relations many-to-many
    skills = models.ManyToManyField(Skills)
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        return super(JobPost, self).save(*args, **kwargs)
    def __str__(self):
        return f'{self.title} zarobki: {self.salary} PLN'

