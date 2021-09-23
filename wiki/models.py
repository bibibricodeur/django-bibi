from django.db import models

# https://docs.djangoproject.com/fr/3.1/intro/tutorial02/

# Cette fonction est utilisée pour formater les URL
from django.urls import reverse

from django.contrib.auth.models import User

# Create your models here.

class WikiCategory(models.Model):
    # Fields
    category_name = models.CharField('Category', max_length=255, unique=True, blank=True, null=True)

    # https://developer.mozilla.org/fr/docs/Learn/Server-side/Django/Models

    # Metadata
    class Meta:
        verbose_name = 'Post Category'
        verbose_name_plural = 'Posts Categories'

    # Methods
    def get_absolute_url(self):
        """Cette fonction est requise pas Django, lorsque vous souhaitez détailler le contenu d'un objet."""
        return reverse('wiki-detail', args=[str(self.id)])

    def __str__(self):
        """Fonction requise par Django pour manipuler les objets dans la base de données."""
        return self.category_name

class WikiPost(models.Model):
    # Fields
    options = (
        ('draft', 'Private'),
        ('published', 'Public'),
    )
    wiki_title = models.CharField('Title', max_length=255)
    wiki_slug = models.SlugField('Slug', max_length=255, unique=True, blank=True, null=True)
    wiki_description = models.CharField('Description', max_length=255, blank=True, null=True)
    wiki_picture = models.ImageField('Head picture', blank=True, null=True, upload_to='wiki')
    wiki_content = models.TextField('Texte')
    wiki_file = models.FileField('File', blank=True, null=True, upload_to='wiki')
    wiki_created = models.DateTimeField('Created', auto_now_add=True)
    wiki_updated = models.DateTimeField('Updated', auto_now=True)

    seo_title = models.SlugField('Seo title', max_length=60, unique=True, blank=True, null=True)
    seo_description = models.SlugField('Seo description', max_length=165, unique=True, blank=True, null=True)

    # https://www.youtube.com/watch?v=_ph8GF84fX4
    wiki_author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author', blank=True, null=True)
    # https://www.youtube.com/watch?v=jFqYuWNyLnI
    wiki_category = models.ForeignKey(WikiCategory, on_delete=models.CASCADE, verbose_name='Category', blank=True, null=True)

    wiki_favorite = models.BooleanField('Favorite', default='False')
    wiki_status = models.CharField('Status', max_length=12, choices=options, default='draft')

    # https://developer.mozilla.org/fr/docs/Learn/Server-side/Django/Models

    # Metadata
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ('wiki_created', )

    # Methods
    def get_absolute_url(self):
        """Cette fonction est requise pas Django, lorsque vous souhaitez détailler le contenu d'un objet."""
        return reverse('wiki-detail', args=[str(self.id)])

    def __str__(self):
        """Fonction requise par Django pour manipuler les objets dans la base de données."""
        return self.wiki_title

### Fin
