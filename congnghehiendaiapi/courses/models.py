from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.

class User(AbstractUser):
     pass



class BaseModel(models.Model):
    created_at = models.DateTimeField( auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)



    class Meta:
        abstract = True



class Course(BaseModel):
    name = models.CharField(max_length=100, null=False, unique=True)
    credits = models.PositiveIntegerField()

    def __str__(self):
        return self.name
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    additional_info = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='courses/%y/%m/')
    def __str__(self):
        return self.full_name
class Lecturer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='courses/%y/%m/')
    additional_info = models.TextField(blank=True)

    def __str__(self):
        return self.full_name
class Syllabus(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
class Assessment(models.Model):
    syllabus = models.ForeignKey(Syllabus, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    max_score = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.syllabus.title} - {self.name}"
class Comment(models.Model):
    syllabus = models.ForeignKey(Syllabus, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.syllabus.title}"
