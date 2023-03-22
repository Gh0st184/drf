from django.db import models

from usersapp.models import MyCustomUser


class Project(models.Model):
    name = models.CharField(verbose_name='Name', max_length=55, unique=True)
    url_repository = models.URLField(verbose_name='Url Repository', blank=True)
    user = models.ManyToManyField(MyCustomUser)


class ToDo(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Text')
    user = models.OneToOneField(MyCustomUser, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)
