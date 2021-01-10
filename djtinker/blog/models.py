from bs4 import BeautifulSoup
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from tinymce import models as tinymce_models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    slug = models.CharField(max_length=60, unique=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save()

    def get_absolute_url(self, *args, **kwargs):
        return reverse('category', kwargs={'slug': self.slug})

    class Meta:
        verbose_name_plural = "Categories"

class Post(models.Model):
    statuses = [
        ('D', 'Draft'),
        ('P', 'Publish')
    ]
    title = models.CharField(max_length=120)
    slug = models.CharField(max_length=60, unique=True, blank=True)
    content = tinymce_models.HTMLField()
    status = models.CharField(max_length=1, choices=statuses)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog/post', default="post-default.jpg", blank=True)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save()

    def get_absolute_url(self, *args, **kwargs):
        return reverse('post-update', kwargs={'slug': self.slug})

    def html_to_text(self, *args, **kwargs):
        soup = BeautifulSoup(self.content, features="html.parser")
        text = soup.get_text()
        return text

    class Meta:
        ordering = ["-date"]

class PostImage(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='blog/post')
    description = models.CharField(max_length=120, default='', blank=True)

    def __str__(self):
        return self.post.title + self.images.name


class Introduction(models.Model):
    statuses = [
        ('A', 'Active'),
        ('I', 'In Active')
    ]
    title = models.CharField(max_length=120)
    message = tinymce_models.HTMLField()
    status = models.CharField(max_length=1, choices=statuses, default='I')

    def __str__(self):
        return self.title

    def html_to_text(self, *args, **kwargs):
        soup = BeautifulSoup(self.message, features="html.parser")
        text = " ".join(soup.find_all(text=True))
        return text
