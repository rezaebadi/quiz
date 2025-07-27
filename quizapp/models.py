from django.db import models
from quizapp.managers import PublishedManager
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType


class Author(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'author'


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, models.DO_NOTHING)

    class Meta:
        db_table = 'book'


class Company(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'company'



class Employee(models.Model):
    name = models.CharField(max_length=255)
    company = models.ForeignKey(Company, models.DO_NOTHING)

    class Meta:
        db_table = 'employee'


class Photo(models.Model):
    file_path = models.CharField(max_length=255)

    class Meta:
        db_table = 'photo'


class Post(models.Model):
    title = models.CharField(max_length=255)
    is_published = models.BooleanField()

    objects = models.Manager() 
    published = PublishedManager() 

    class Meta:
        db_table = 'post'


class Profile(models.Model):
    user = models.OneToOneField(User, models.DO_NOTHING)
    bio = models.TextField()

    class Meta:
        db_table = 'profile'


class Survey(models.Model):
    questions_json = models.JSONField()

    class Meta:
        db_table = 'survey'


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = 'tag'


class Taggeditem(models.Model):
    tag = models.ForeignKey(Tag, models.DO_NOTHING)
    content_type = models.ForeignKey(ContentType, models.DO_NOTHING)
    object_id = models.IntegerField()

    class Meta:
        db_table = 'taggeditem'


class Tenant(models.Model):
    schema_name = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = 'tenant'
