from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey


class CategoryProjects(MPTTModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    parent = TreeForeignKey(
        'self',
        related_name="children",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']


class Projects(models.Model):
    slug = models.SlugField(max_length=100, default='', unique=True)
    author = models.ForeignKey(User, related_name='projects', on_delete=models.SET_NULL, null=True)
    title = models.TextField(max_length=100)
    image = models.ImageField(upload_to='articles/')
    text = models.TextField(max_length=400)
    category = models.ForeignKey(
        CategoryProjects,
        related_name='project',
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project_single', kwargs={"slug": self.category.slug, 'project_slug': self.slug})

    def get_image(self):
        return self.projectimages.all()


class ProjectImage(models.Model):
    images = models.ImageField(upload_to='articles/')
    projects = models.ForeignKey(Projects, related_name='projectimages', on_delete=models.SET_NULL, null=True)


class Reviews(models.Model):
    name = models.CharField(max_length=50)
    massage = models.TextField(max_length=500)

    def __str__(self):
        return self.name


class Employees(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    images = models.FileField(upload_to='articles/')

    def __str__(self):
        return self.name


class ContactModel(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя')
    numbers = models.IntegerField(verbose_name='Номер телефона')
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.numbers}'


class PartnersModel(models.Model):
    img = models.FileField(upload_to='articles/')
    name = models.CharField(max_length=200, verbose_name='Имя')

    def __str__(self):
        return self.name
