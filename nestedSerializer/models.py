from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    age = models.IntegerField()
    image = models.ImageField(upload_to="",blank=True)
    def __str__(self):
        return self.name
    
    
class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    post_date = models.DateField(("date"), auto_now_add=True)
    post_time = models.TimeField(("time"), auto_now_add=True)
    image = models.ImageField(upload_to="",blank=True)
    author = models.ForeignKey(Author, related_name="posts", on_delete=models.CASCADE)
   
    def __str__(self):
       return self.author.name
