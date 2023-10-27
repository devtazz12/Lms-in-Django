from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    images = models.ImageField(upload_to="images", null=True)

    def __str__(self):
        return self.name
    


class Course(models.Model):
    name=models.CharField(max_length=100)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    image=models.ImageField(upload_to="images", null=True)
    price=models.IntegerField()
    
    def __str__(self):
        return self.name

class Lecture(models.Model):
    name=models.CharField(max_length=300)
    course=models.ForeignKey(Course, on_delete=models.CASCADE)
    video = models.FileField(upload_to="videos")
    duration = models.CharField( max_length=10, null=True)
    preview=models.BooleanField(default=False)
    thumbnail = models.ImageField(upload_to="thumbnail", null=True)


    def __str__(self):
        return self.name
    

class MyCourses(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name=models.CharField(max_length=100)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    image=models.ImageField(upload_to="images", null=True)
    courseid=models.IntegerField(null=True)

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    fullname= models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.fullname



    

    
    

    
    

    


    
