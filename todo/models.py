from django.db import models

# https://docs.djangoproject.com/fr/3.1/intro/tutorial02/

# Cette fonction est utilisée pour formater les URL
from django.urls import reverse

from django.contrib.auth.models import User

# Create your models here.

class TodoCategory(models.Model):
    # Fields
    category_name = models.CharField('Category', max_length=255)

    # https://developer.mozilla.org/fr/docs/Learn/Server-side/Django/Models

    # Metadata
    class Meta:
        verbose_name = 'Todo Category'
        verbose_name_plural = 'Todos Categories'

    # Methods
    def get_absolute_url(self):
        """Cette fonction est requise pas Django, lorsque vous souhaitez détailler le contenu d'un objet."""
        return reverse('todo-detail', args=[str(self.id)])

    def __str__(self):
        """Fonction requise par Django pour manipuler les objets dans la base de données."""
        return self.category_name

class TodoPost(models.Model):
    # Fields
    options = (
        ('draft', 'Private'),
        ('published', 'Public'),
    )
    todo_title = models.CharField('Title', max_length=255)
    todo_description = models.TextField('Description', blank=True, null=True)
    todo_created = models.DateTimeField('Created', auto_now_add=True)
    todo_updated = models.DateTimeField('Updated', auto_now=True)
    todo_favorite = models.BooleanField('Favorite', default='False')
    todo_completed = models.BooleanField('Completed', default='False')

    # https://www.youtube.com/watch?v=_ph8GF84fX4
    todo_author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author', blank=True, null=True)
    # https://www.youtube.com/watch?v=jFqYuWNyLnI
    todo_category = models.ForeignKey(TodoCategory, on_delete=models.CASCADE, verbose_name='Category', blank=True, null=True)

    todo_status = models.CharField('Status', max_length=12, choices=options, default='draft')

    # https://developer.mozilla.org/fr/docs/Learn/Server-side/Django/Models

    # Metadata
    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'
        ordering = ('todo_created', )

    # Methods
    def get_absolute_url(self):
        """Cette fonction est requise pas Django, lorsque vous souhaitez détailler le contenu d'un objet."""
        return reverse('todo-detail', args=[str(self.id)])

    def __str__(self):
        """Fonction requise par Django pour manipuler les objets dans la base de données."""
        return self.todo_title

### Fin
