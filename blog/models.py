from django.db import models

# https://docs.djangoproject.com/fr/3.1/intro/tutorial02/

# Cette fonction est utilisée pour formater les URL
from django.urls import reverse

from django.contrib.auth.models import User

# Create your models here.

class BlogCategory(models.Model):
    # Fields
    category_name = models.CharField('Category', max_length=255, unique=True, blank=True, null=True)
    category_slug = models.SlugField('Slug', max_length=255, unique=True, blank=True, null=True)

    # https://developer.mozilla.org/fr/docs/Learn/Server-side/Django/Models

    # Metadata
    class Meta:
        verbose_name = 'Post Category'
        verbose_name_plural = 'Posts Categories'

    # Methods
    def get_absolute_url(self):
        """Cette fonction est requise pas Django, lorsque vous souhaitez détailler le contenu d'un objet."""
        return reverse('blog-detail', args=[str(self.id)])

    def __str__(self):
        """Fonction requise par Django pour manipuler les objets dans la base de données."""
        return self.category_name


class BlogPost(models.Model):
    # Fields
    options = (
        ('draft', 'Private'),
        ('published', 'Public'),
    )
    blog_title = models.CharField('Title', max_length=255)
    blog_slug = models.SlugField('Slug', max_length=255, unique=True, blank=True, null=True)
    blog_description = models.CharField('Description', max_length=255, blank=True, null=True)
    blog_picture = models.ImageField('Head picture', blank=True, null=True, upload_to='blog')
    blog_content = models.TextField('Texte')
    blog_file = models.FileField('File', blank=True, null=True, upload_to='blog')
    blog_created = models.DateTimeField('Created', auto_now_add=True)
    blog_updated = models.DateTimeField('Updated', auto_now=True)

    seo_title = models.SlugField('Seo title', max_length=60, unique=True, blank=True, null=True)
    seo_description = models.SlugField('Seo description', max_length=165, unique=True, blank=True, null=True)

    # https://www.youtube.com/watch?v=_ph8GF84fX4
    blog_author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author', blank=True, null=True)
    # https://www.youtube.com/watch?v=jFqYuWNyLnI
    blog_category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, verbose_name='Category', blank=True, null=True)

    blog_favorite = models.BooleanField('Favorite', default='False')
    blog_status = models.CharField('Status', max_length=12, choices=options, default='draft')

    # https://developer.mozilla.org/fr/docs/Learn/Server-side/Django/Models

    # Metadata
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ('blog_created', )

    # Methods
    def get_absolute_url(self):
        """Cette fonction est requise pas Django, lorsque vous souhaitez détailler le contenu d'un objet."""
        return reverse('blog-detail', args=[str(self.id)])

    def __str__(self):
        """Fonction requise par Django pour manipuler les objets dans la base de données."""
        return self.blog_title

### Fin
