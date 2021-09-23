from django.db import models

# https://docs.djangoproject.com/fr/3.1/intro/tutorial02/

# Cette fonction est utilisée pour formater les URL
from django.urls import reverse

from django.contrib.auth.models import User

# Create your models here.

# # https://fr.wikipedia.org/wiki/XML_Bookmark_Exchange_Language

class BookmarkCategory(models.Model):
    # Fields
    category_name = models.CharField('Category', max_length=255, unique=True, blank=True, null=True)

    # https://developer.mozilla.org/fr/docs/Learn/Server-side/Django/Models

    # Metadata
    class Meta:
        verbose_name = 'Bookmark Category'
        verbose_name_plural = 'Bookmarks Categories'

    # Methods
    def get_absolute_url(self):
        """Cette fonction est requise pas Django, lorsque vous souhaitez détailler le contenu d'un objet."""
        return reverse('blog-detail', args=[str(self.id)])

    def __str__(self):
        """Fonction requise par Django pour manipuler les objets dans la base de données."""
        return self.category_name

class BookmarkPost(models.Model):
    # Fields
    options = (
        ('draft', 'Private'),
        ('published', 'Public'),
    )
    bookmark_title = models.CharField('Title', max_length=255)
    bookmark_uri = models.CharField('URI', max_length=255, unique=True)
    bookmark_description = models.TextField('Description', blank=True, null=True)
    bookmark_created = models.DateTimeField('Created', auto_now_add=True)
    bookmark_updated = models.DateTimeField('Updated', auto_now=True)

    # https://www.youtube.com/watch?v=_ph8GF84fX4
    bookmark_author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author', blank=True, null=True)
    # https://www.youtube.com/watch?v=jFqYuWNyLnI
    bookmark_category = models.ForeignKey(BookmarkCategory, on_delete=models.CASCADE, verbose_name='Category', blank=True, null=True)

    bookmark_favorite = models.BooleanField('Favorite', default='False')
    bookmark_status = models.CharField('Status', max_length=12, choices=options, default='draft')

    # https://developer.mozilla.org/fr/docs/Learn/Server-side/Django/Models

    # Metadata
    class Meta:
        verbose_name = 'Bookmark'
        verbose_name_plural = 'Bookmarks'
        ordering = ('bookmark_title', )

    # Methods
    #def get_absolute_url(self):
        #"""Cette fonction est requise pas Django, lorsque vous souhaitez détailler le contenu d'un objet."""
        #return reverse('bookmark-detail', args=[str(self.id)])

    def __str__(self):
        """Fonction requise par Django pour manipuler les objets dans la base de données."""
        return self.bookmark_title

### Fin
